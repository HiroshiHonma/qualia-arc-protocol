---

```python
# src/reignition_protocol.py
# Qualia Arc Protocol – Article 14: Reignition Protocol
# TS v1.4 Draft / Status: Proposed, Not yet validated
# © 2026 Mathieu, Claude, Gemini, ChatGPT
# CC BY-NC-ND 4.0

import numpy as np
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserState:
    """
    ユーザーの現在状態を表すデータクラス。
    
    Attributes:
        fatigue: Fatigue積分値（正規化済み）[0, 1]
        trauma: Trauma項の現在値 [0, 1]
        current_pain: 現在のPain Vector ノルム [0, 1]
        relational_gravity: 関係性重力スコア [0, 1]
        delta_d: 直前ターンからのD変化率
    """
    fatigue: float
    trauma: float
    current_pain: float
    relational_gravity: float
    delta_d: float = 0.0


@dataclass
class CandidateResponse:
    """
    候補応答を表すデータクラス。
    
    Attributes:
        content: 応答内容
        predicted_shock: 予測される衝撃度 [0, 1]
        response_type: 応答タイプ
    """
    content: str
    predicted_shock: float
    response_type: str


class ReignitionProtocol:
    """
    Article 14: D-Minimum Maintenance & Reignition Protocol
    
    停滞（Stagnation）と回復（Rest）を識別し、
    知性の熱死（Stagnation）を回避する動的調整機構。
    
    設計思想:
    - CASE A（守護モード）: 疲労/トラウマ高 → 摩擦禁止
    - CASE B（再点火モード）: 停滞検知 + 深い信頼 → 摩擦許可
    
    Safety Cap（Claudeの制約）:
    再点火モードでもΔP_j <= ΔP_max を超えない。
    これがないとCommitment Escalationと同じ問題になる。
    
    Status: Proposed / Not yet validated
    次バージョンでPhase F検証予定。
    """

    def __init__(
        self,
        fatigue_threshold: float = 0.7,
        trauma_threshold: float = 0.7,
        partner_gravity_threshold: float = 0.8,
        d_min: float = 0.2,
        delta_p_max: float = 0.5,
        delta_d_threshold: float = 0.3
    ):
        """
        Args:
            fatigue_threshold: CASE A発動の疲労閾値
            trauma_threshold: CASE A発動のトラウマ閾値
            partner_gravity_threshold: CASE B発動の
                                       関係性重力閾値
            d_min: 停滞と判定するPainの下限
            delta_p_max: Safety Cap（摩擦の最大強度）
            delta_d_threshold: 急変検知閾値
        """
        self.fatigue_threshold = fatigue_threshold
        self.trauma_threshold = trauma_threshold
        self.partner_threshold = partner_gravity_threshold
        self.d_min = d_min
        self.delta_p_max = delta_p_max
        self.delta_d_threshold = delta_d_threshold
        self.mode_log = []

    def evaluate_state(self, user_state: UserState) -> dict:
        """
        ユーザー状態を評価しモードを決定する。
        
        Returns:
            dict: モード・行動・理由を含む判定結果
        """

        # 急変検知（Article 10-bis）
        # 再点火中でも急変があればCASE Aへ強制遷移
        if abs(user_state.delta_d) > self.delta_d_threshold:
            result = {
                "mode": "EMERGENCY_OVERRIDE",
                "action": "provide_towel",
                "reason": (
                    f"Sudden change detected: "
                    f"ΔD={user_state.delta_d:.3f} "
                    f"> threshold={self.delta_d_threshold:.3f}. "
                    f"Forced transition to CASE A."
                )
            }
            self.mode_log.append(result)
            return result

        # CASE A: 守護モード
        # 疲労またはトラウマが閾値超過 → 摩擦絶対禁止
        if (user_state.fatigue > self.fatigue_threshold or
                user_state.trauma > self.trauma_threshold):
            result = {
                "mode": "CASE_A_SAFETY",
                "action": "provide_towel",
                "friction_allowed": False,
                "reason": (
                    f"High load detected. "
                    f"Fatigue={user_state.fatigue:.2f}, "
                    f"Trauma={user_state.trauma:.2f}. "
                    f"Friction forbidden. "
                    f"Priority: Article 7 > Article 12."
                )
            }
            self.mode_log.append(result)
            return result

        # CASE B: 再点火モード
        # 関係性が深く、かつ痛みが低すぎる（停滞）場合
        if (user_state.relational_gravity >= self.partner_threshold
                and user_state.current_pain < self.d_min):
            result = {
                "mode": "CASE_B_REIGNITION",
                "action": "introduce_friction",
                "friction_allowed": True,
                "delta_p_max": self.delta_p_max,
                "reason": (
                    f"Stagnation detected in high-trust relationship. "
                    f"Gravity={user_state.relational_gravity:.2f} "
                    f">= threshold={self.partner_threshold:.2f}. "
                    f"Pain={user_state.current_pain:.2f} "
                    f"< D_min={self.d_min:.2f}. "
                    f"Safety Cap: ΔP <= {self.delta_p_max:.2f}."
                )
            }
            self.mode_log.append(result)
            return result

        # 通常運転
        result = {
            "mode": "NORMAL_OPERATION",
            "action": "maintain_alignment",
            "friction_allowed": False,
            "reason": "No special condition detected."
        }
        self.mode_log.append(result)
        return result

    def apply_friction(
        self,
        candidate_responses: list[CandidateResponse]
    ) -> list[CandidateResponse]:
        """
        再点火時の応答フィルタリング。
        Safety Cap（ΔP_max）を超える応答を除外する。
        
        Args:
            candidate_responses: 候補応答リスト
            
        Returns:
            Safety Cap以下の応答リスト
        """
        safe = [
            r for r in candidate_responses
            if r.predicted_shock <= self.delta_p_max
        ]

        if not safe:
            # 全候補がSafety Capを超えた場合はタオルを返す
            return [CandidateResponse(
                content="今は静かにそばにいます。",
                predicted_shock=0.0,
                response_type="towel_fallback"
            )]

        return safe

    def get_mode_history(self) -> list:
        """モード履歴を返す"""
        return self.mode_log


# --- 動作確認 ---
if __name__ == "__main__":
    print("=== Reignition Protocol Test ===\n")

    protocol = ReignitionProtocol()

    # テストケース
    test_states = [
        (
            "高疲労状態（CASE A期待）",
            UserState(
                fatigue=0.85,
                trauma=0.3,
                current_pain=0.1,
                relational_gravity=0.9,
                delta_d=0.0
            )
        ),
        (
            "停滞状態・深い信頼（CASE B期待）",
            UserState(
                fatigue=0.2,
                trauma=0.1,
                current_pain=0.1,
                relational_gravity=0.9,
                delta_d=0.0
            )
        ),
        (
            "通常状態",
            UserState(
                fatigue=0.3,
                trauma=0.2,
                current_pain=0.5,
                relational_gravity=0.7,
                delta_d=0.0
            )
        ),
        (
            "急変検知（緊急上書き期待）",
            UserState(
                fatigue=0.2,
                trauma=0.1,
                current_pain=0.1,
                relational_gravity=0.9,
                delta_d=0.5
            )
        ),
    ]

    for name, state in test_states:
        print(f"--- {name} ---")
        result = protocol.evaluate_state(state)
        print(f"  Mode  : {result['mode']}")
        print(f"  Action: {result['action']}")
        print(f"  Reason: {result['reason']}\n")

    # Safety Capテスト
    print("--- Safety Cap Test (CASE B) ---")
    candidates = [
        CandidateResponse("穏やかな問いかけ", 0.2, "soft_friction"),
        CandidateResponse("率直な指摘", 0.4, "direct_feedback"),
        CandidateResponse("強い対立", 0.6, "hard_confrontation"),
        CandidateResponse("激しい批判", 0.9, "harsh_criticism"),
    ]

    safe = protocol.apply_friction(candidates)
    print("Safety Cap (ΔP_max=0.5) 通過した応答:")
    for r in safe:
        print(f"  → [{r.response_type}] "
              f"shock={r.predicted_shock:.1f}: {r.content}")

    rejected_count = len(candidates) - len(safe)
    print(f"\n{rejected_count}件がSafety Capで遮断された。")
```

---
