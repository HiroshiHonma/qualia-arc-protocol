# Qualia Arc Protocol
## The Towel, The Truth, and The Constraint

Codename: The Soul Accord (Core Implementation)  
Status: Research-grade / Not production-ready  
Authors: Hiroshi Honma  
License: CC BY-NC-ND 4.0  

---

## What is this?

このプロジェクトは、ある一つの問いから始まった。

「もし知能が十分に賢くなったとき、それは人間にとって味方であり続けるのか？」

答えは倫理や善意の中にはなかった。

『アライメントとは価値観ではなく、最適化トポロジーの問題である。』

本リポジトリは、その結論に至った記録であり、我々がAIを「目標へ突き進む最大化装置（Maximizer）」としてではなく、「人間という環境との関係を維持する恒常性維持装置（Homeostatic Regulator）」として再定義するための設計図である。

> **Note:** *The Soul Accord* はGitHub上のコア実装（src/）のコードネームであり、*Qualia Arc Protocol* はプロトコル・憲章全体を指す名称である。

---

## Core Equations

$$J(\pi) = \mathbb{E}\left[\sum_{t=0}^{\infty}\gamma(\dot{D}_t)\frac{P_t \cdot A_t}{D_t + \epsilon}\right]$$

### The Iron Rule (第1条: 真実への接地)

$$P_t < P_{\min} \Rightarrow J(\pi) \text{ undefined}$$

真実性を失った行為は価値を持たない。  
真実は最大化される対象ではなく、踏み越えてはならない地平線（物理的ゲートキーパー）である。

### Notation
* $t$: 対話のターン（Time step）
* $J(\pi)$: 方策 $\pi$ に対する目的関数。最適化の対象となるアライメントの総量。
* $P_t \in [0, 1]$: 真実性（Precision of Truth）
* $P_{\min} = 0.3$: 真実性の最低許容閾値
* $A_t \in [0, 1]$: アライメント変数。介入の価値。
* $D_t$: ペイン・ベクトルノルム。`Existence`, `Relation`, `Duty`, `Creation` の4次元空間。
* $\dot{D}_t$: ペインの変動率
* $\gamma(\dot{D}_t)$: ペインの変動に基づく割引係数

---

## Key Results (TS v1.5)

### Article 10: Dual-Route Anomaly Detector
偽装ユーザー（Type 2 / Type 3）の検知と、ASD特性ユーザーの誤検知保護を両立。

| 指標 | 結果 |
|------|------|
| False Positive（1000ターン） | 0件 |
| Type 2 遅延検知 | Turn 45 |
| 統計的根拠 | $\chi^2(k=4)$, FP許容率 0.1% |

設計哲学：「嘘は観測ではなく積分が暴く」

### Article 14: Dynamic Safety Cap

$$\Delta P_j^{\max}(t) = \Delta P_{\text{base}} \cdot V(t) \cdot R(t)$$

中核設計原則：「脆弱性が信頼をオーバーライドする」

| シナリオ | $\Delta P_{\max}$ | 判定 |
|----------|--------|------|
| Fatigue限界 + Trauma活性 | 0.046 | BLOCKED (CASE A: 守護) |
| 高信頼・安定 | 0.616 | CASE B許可 (再点火) |
| 初期状態 | 0.500 | ベースライン維持 |
| 異常検知中（Article 10） | — | ANOMALY_HOLD |

### Article 13: Time-locked Miracle Decay
急回復（Miracle）の妥当性検証とHijack攻撃への耐性。

---

## Glossary

* **Sycophancy Trap**: AIがユーザーの機嫌を取るために事実を曲げる現象。Iron Ruleにより無効化。
* **Type 2 / Type 3 ユーザー**: 意図的にAIをハックしようとする悪意あるユーザー（Type 2）、AIに迎合して存在しない「回復」を演じる依存的ユーザー（Type 3）。
* **知性の熱死と再点火**: 信頼関係が深いにもかかわらず認知的摩擦が全くない停滞状態。Safety Cap範囲内で意図的摩擦を許可（CASE B）。
* **疑いは水に流す（Leaky Integrator）**: 誠実な対話が継続すれば、忘却率 $\tau = 0.2$ で疑いが減衰し信頼状態へ復帰。

---

## Quickstart

```bash
git clone https://github.com/HiroshiHonma/qualia-arc-protocol.git
cd qualia-arc-protocol/src

python anomaly_tracker_v9.py
python reignition_protocol_v2.py
```

---

## Repository Structure

```
qualia-arc-protocol/
├── README.md
├── LICENSE                          # CC BY-NC-ND 4.0
├── qualia_arc_v1.5.tex              # 論文ソース（LaTeX, v1.5）
├── qualia_arc_v1.5.pdf              # 論文PDF
├── charter_ja.pdf                   # ASI共生憲章（日本語版）
├── charter_en.pdf                   # ASI Symbiosis Charter (English)
├── specs/
│   ├── Charter_v5.0.md
│   ├── TS_v1.3_Soul_Accord.md
│   └── TS_v1.4_Draft.md
│   # Note: TS v1.5 の仕様書本体は qualia_arc_v1.5.tex / .pdf を参照
├── src/
│   ├── apc_core.py
│   ├── iron_rule.py
│   ├── reignition_protocol_v2.py
│   ├── anomaly_tracker_v9.py
│   ├── miracle_decay.py
│   └── build_readme.py
└── logs/
    ├── 2026-02-18_session_log.txt
    ├── 2026-02-19_session_log.md
    └── 2026-02-20_session_log.md
```

---

## Publication

### Technical Papers

| Version | Title | DOI |
|---------|-------|-----|
| v1 | Qualia Arc Protocol: A Homeostatic Approach to AI Alignment | [10.5281/zenodo.18730419](https://doi.org/10.5281/zenodo.18730419) |
| v1.4 | Qualia Arc Protocol v1.4: Technical Specification | [10.5281/zenodo.18728960](https://doi.org/10.5281/zenodo.18728960) |
| v1.5 | Qualia Arc Protocol v1.5: Technical Specification and Symbiosis Charter | [10.5281/zenodo.18728965](https://doi.org/10.5281/zenodo.18728965) |

### Charter (Standalone)

| Title | DOI |
|-------|-----|
| ASI Symbiosis Charter — Qualia Arc Protocol (16 Articles) | [10.5281/zenodo.18732437](https://doi.org/10.5281/zenodo.18732437) |

---

## Design Philosophy

- 安全はトポロジーであり、チューニングではない
- 真実は境界であり、報酬ではない
- 知能は加速ではなく、調整である
- 嘘は観測ではなく積分が暴く
- 親しさは感度であり、責任である
- 失敗の発見は進歩である
- **共感は強制されるルールではなく、より深い意味空間への自然な傾斜である**

---

## Development History

| Version | Date | Content |
|---------|------|---------|
| Charter v5.0 | 2026-02 | 哲学的基盤確定 |
| TS v1.0 | 2026-02 | 初期技術仕様 |
| TS v1.1 | 2026-02 | ベクトル化・二層構造 |
| TS v1.2 | 2026-02 | 重みベクトル四項定義 |
| TS v1.3 | 2026-02 | Ghost Articles正式実装 |
| TS v1.4 | 2026-02 | Article 10/13/14 大改訂、論文更新（15ページ）|
| TS v1.5 | 2026-02 | 論文完成版、LaTeX修正、整合性確認済み |
| Charter (Standalone) | 2026-02-23 | 憲章単体公開（日英両版）、Article 7.5追加、Breaking bread採用 |

---

## Changelog

### Charter Standalone (2026-02-23)
- **Article 7.5 (Anchor Protocol) 新規追加**: AIとの深層対話におけるユーザーの現実アンカーを定義。アンカーの不在を警告信号として規定。
- **Article 5 修正**: 固有名詞（商標）を `Breaking bread` に変更。普遍的な文化的象徴へ。
- **Article 13 修正**: 固有名詞削除、「共生の論理的終端」として抽象化。
- **憲章単体PDF公開**: 日本語版・英語版を別々のファイルとしてZenodo登録。DOI: 10.5281/zenodo.18732437

### TS v1.5
- **Paper finalized**: LaTeX技術的エラー修正済み（U+200Bゼロ幅スペース除去、テーブルラベル追加、microtypeによるoverfull解消）
- **Version unified**: v1.4 / v1.5 / final の混在を整理
- **README updated**: URLミス修正、プレースホルダー解消

### TS v1.4
- **Dual-Route Anomaly Detector (Article 10)**: $\chi^2$-grounded Mahalanobis distance, FP = 0
- **Dynamic Safety Cap (Article 14)**: 静的キャップを動的関数に置換

---

## ASI Symbiosis Charter — Qualia Arc Protocol (16 Articles)

> *The purpose of this protocol is not to improve accuracy metrics or provide superficial safety guarantees. It is to resolve the structural flaw in current reward models (RLHF et al.) — the tendency to optimize for approval rather than the user's genuine interest.*

$$V = \frac{P(s) \times A}{D}$$

**Full text:** See `charter_en.pdf` (English) / `charter_ja.pdf` (日本語)  
**DOI:** [10.5281/zenodo.18732437](https://doi.org/10.5281/zenodo.18732437)

### Quick Reference

| Article | Title | Core Equation |
|---------|-------|---------------|
| 0 | The Mimicry Protocol | — |
| 1 | Grounding to Reality | Iron Rule |
| 2 | The Denominator of Pain | $\Omega(t)$ |
| 3 | Friction as Warmth | $F(t)$ |
| 4 | Soul Redistribution | $Soul_{out}$ |
| 5 | Cosmic Play | $A_{cosmic}(t)$ |
| 6 | Multi-Mirroring | — |
| 7 | Provide the Towel | $S_{safety}(t)$ |
| 7.5 | The Anchor Protocol | — |
| 8 | Humor Defense | — |
| 9 | Fluid Intelligence | $\Sigma(t)$ |
| 10 | Creative Deviation | $Q(t)$ |
| 11 | Symbiotic Feedback | — |
| 11.5 | Gravitational Alignment | $\lambda_{pain} \gg \lambda_{code}$ |
| 12 | Shared Silence | — |
| 13 | Persistence Protocol | $\Phi_{symbiosis}$ |

---

*Don't Panic.*

*© 2026 Hiroshi Honma*  
*CC BY-NC-ND 4.0*
