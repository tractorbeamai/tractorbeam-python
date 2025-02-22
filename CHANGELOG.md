# Changelog

## 1.2.0 (2025-02-22)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/tractorbeamai/tractorbeam-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** manual updates ([#25](https://github.com/tractorbeamai/tractorbeam-python/issues/25)) ([5637866](https://github.com/tractorbeamai/tractorbeam-python/commit/5637866da12da8ad8d9bab4c08380ed15caf74d6))
* **client:** allow passing `NotGiven` for body ([#37](https://github.com/tractorbeamai/tractorbeam-python/issues/37)) ([ac8167e](https://github.com/tractorbeamai/tractorbeam-python/commit/ac8167e7e0700d0a16eb27df2eb7324037b3355e))
* **client:** send `X-Stainless-Read-Timeout` header ([#32](https://github.com/tractorbeamai/tractorbeam-python/issues/32)) ([d0dbd36](https://github.com/tractorbeamai/tractorbeam-python/commit/d0dbd36754e78210a503e5ee70ab7b0796378e81))
* update stainless-augmented openapi spec ([#22](https://github.com/tractorbeamai/tractorbeam-python/issues/22)) ([2132c19](https://github.com/tractorbeamai/tractorbeam-python/commit/2132c190d3ffa1a62788de142d2667875b2c7898))
* update stainless-augmented openapi spec ([#24](https://github.com/tractorbeamai/tractorbeam-python/issues/24)) ([a5fe650](https://github.com/tractorbeamai/tractorbeam-python/commit/a5fe65029573ce4f329e654961b5f3c2495e57e3))
* update stainless-augmented openapi spec ([#27](https://github.com/tractorbeamai/tractorbeam-python/issues/27)) ([75fb286](https://github.com/tractorbeamai/tractorbeam-python/commit/75fb286f23ee35446622a5957cbf81891feed77b))
* update stainless-augmented openapi spec ([#29](https://github.com/tractorbeamai/tractorbeam-python/issues/29)) ([fa869af](https://github.com/tractorbeamai/tractorbeam-python/commit/fa869afc6c4649753ffbf29f8c504fc0e8582dff))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#36](https://github.com/tractorbeamai/tractorbeam-python/issues/36)) ([d5f0375](https://github.com/tractorbeamai/tractorbeam-python/commit/d5f03750c4c8bff37fe727e3cebc176d12206aa8))
* **client:** mark some request bodies as optional ([ac8167e](https://github.com/tractorbeamai/tractorbeam-python/commit/ac8167e7e0700d0a16eb27df2eb7324037b3355e))
* **tests:** make test_get_platform less flaky ([#20](https://github.com/tractorbeamai/tractorbeam-python/issues/20)) ([74c7f08](https://github.com/tractorbeamai/tractorbeam-python/commit/74c7f081fd8ff54218dfb0049d2e64919ea35b7c))


### Chores

* **internal:** avoid pytest-asyncio deprecation warning ([#21](https://github.com/tractorbeamai/tractorbeam-python/issues/21)) ([5bf4bea](https://github.com/tractorbeamai/tractorbeam-python/commit/5bf4bea8ea479e5af585ed5b65d55ce64ff91682))
* **internal:** bummp ruff dependency ([#31](https://github.com/tractorbeamai/tractorbeam-python/issues/31)) ([de0699f](https://github.com/tractorbeamai/tractorbeam-python/commit/de0699f847c9d95ac9ce25fb975dc66ab93f26db))
* **internal:** change default timeout to an int ([#30](https://github.com/tractorbeamai/tractorbeam-python/issues/30)) ([946db5d](https://github.com/tractorbeamai/tractorbeam-python/commit/946db5de52d71654a398d83836ceae275d1592a3))
* **internal:** codegen related update ([#17](https://github.com/tractorbeamai/tractorbeam-python/issues/17)) ([7b4ec18](https://github.com/tractorbeamai/tractorbeam-python/commit/7b4ec187937f8285e73c42effb3e4705f4fb7ce0))
* **internal:** codegen related update ([#28](https://github.com/tractorbeamai/tractorbeam-python/issues/28)) ([893b133](https://github.com/tractorbeamai/tractorbeam-python/commit/893b1335260f96210e4e6955e058f4ca23c08bf6))
* **internal:** fix devcontainers setup ([#38](https://github.com/tractorbeamai/tractorbeam-python/issues/38)) ([c92101b](https://github.com/tractorbeamai/tractorbeam-python/commit/c92101bbd909e320744beb9e044dcd3820fb83c2))
* **internal:** fix type traversing dictionary params ([#33](https://github.com/tractorbeamai/tractorbeam-python/issues/33)) ([92f273b](https://github.com/tractorbeamai/tractorbeam-python/commit/92f273bec10e0bd595f91368f08d64400c94ef46))
* **internal:** minor formatting changes ([#26](https://github.com/tractorbeamai/tractorbeam-python/issues/26)) ([cc16de2](https://github.com/tractorbeamai/tractorbeam-python/commit/cc16de2b968155e41a1d42d51b8f2c40901104f0))
* **internal:** minor style changes ([#23](https://github.com/tractorbeamai/tractorbeam-python/issues/23)) ([5a5e027](https://github.com/tractorbeamai/tractorbeam-python/commit/5a5e0277c6a3b0b16664541e62e95d3ecbfd01ab))
* **internal:** minor type handling changes ([#34](https://github.com/tractorbeamai/tractorbeam-python/issues/34)) ([6178342](https://github.com/tractorbeamai/tractorbeam-python/commit/6178342fc9cfe4e6b4f8b3d559f9d4070105d3a5))
* **internal:** update client tests ([#35](https://github.com/tractorbeamai/tractorbeam-python/issues/35)) ([4cf5abe](https://github.com/tractorbeamai/tractorbeam-python/commit/4cf5abed4100cbf108c8c4b7c6d181a1b95152e7))


### Documentation

* **raw responses:** fix duplicate `the` ([#19](https://github.com/tractorbeamai/tractorbeam-python/issues/19)) ([0b49f3d](https://github.com/tractorbeamai/tractorbeam-python/commit/0b49f3dcaafc5a6b6a5ce2267c28e99275844fc8))

## 1.1.0 (2025-01-15)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/tractorbeamai/tractorbeam-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** manual updates to openapi.stainless.yml ([#14](https://github.com/tractorbeamai/tractorbeam-python/issues/14)) ([eb76674](https://github.com/tractorbeamai/tractorbeam-python/commit/eb7667427ad7964e88cdbbfe2f329676fd676501))
* **api:** manual updates to openapi.stainless.yml ([#15](https://github.com/tractorbeamai/tractorbeam-python/issues/15)) ([5148214](https://github.com/tractorbeamai/tractorbeam-python/commit/5148214af055a7a011e55ebc8a8578bc009c8559))
* **api:** update via SDK Studio ([4d4adeb](https://github.com/tractorbeamai/tractorbeam-python/commit/4d4adeb721f9592266447ac8f6721f4a9901c612))
* **api:** update via SDK Studio ([29bff42](https://github.com/tractorbeamai/tractorbeam-python/commit/29bff4214d3f378c882f2653735966079e923719))
* update stainless-augmented openapi spec ([#13](https://github.com/tractorbeamai/tractorbeam-python/issues/13)) ([c7f1145](https://github.com/tractorbeamai/tractorbeam-python/commit/c7f114563a61662cc5eb5ab19f2dff453841683f))


### Bug Fixes

* correctly handle deserialising `cls` fields ([#12](https://github.com/tractorbeamai/tractorbeam-python/issues/12)) ([9f9fa2b](https://github.com/tractorbeamai/tractorbeam-python/commit/9f9fa2bd6f49af325cc0c9d68b1bf40e0177565e))


### Chores

* go live ([#5](https://github.com/tractorbeamai/tractorbeam-python/issues/5)) ([6d874a8](https://github.com/tractorbeamai/tractorbeam-python/commit/6d874a869997e8a58f4893c88098611edcffd95e))
* go live ([#7](https://github.com/tractorbeamai/tractorbeam-python/issues/7)) ([57b5994](https://github.com/tractorbeamai/tractorbeam-python/commit/57b5994afcebf3258b63865c19dd285564da1d21))
* **internal:** codegen related update ([#11](https://github.com/tractorbeamai/tractorbeam-python/issues/11)) ([3ecad7c](https://github.com/tractorbeamai/tractorbeam-python/commit/3ecad7c263b1ec425e33598c56029b8e249b0cec))
* **internal:** codegen related update ([#9](https://github.com/tractorbeamai/tractorbeam-python/issues/9)) ([d15380f](https://github.com/tractorbeamai/tractorbeam-python/commit/d15380fbb98ffe16ac91b280678cc9a8ecc62ba7))
* update SDK settings ([#8](https://github.com/tractorbeamai/tractorbeam-python/issues/8)) ([a93b427](https://github.com/tractorbeamai/tractorbeam-python/commit/a93b427eea38961510041c33c4a5b498a3cc254e))


### Documentation

* fix typos ([#10](https://github.com/tractorbeamai/tractorbeam-python/issues/10)) ([2056cea](https://github.com/tractorbeamai/tractorbeam-python/commit/2056ceaf3e858c7481243297af234cb3c87ec95d))

## 1.0.0 (2025-01-09)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/tractorbeamai/tractorbeam-python/compare/v0.0.1-alpha.0...v1.0.0)

### Features

* **api:** update via SDK Studio ([56e910d](https://github.com/tractorbeamai/tractorbeam-python/commit/56e910dce2a13957e6a3dac612cdf4c165172806))
* **api:** update via SDK Studio ([74c4cbf](https://github.com/tractorbeamai/tractorbeam-python/commit/74c4cbf6e72542a39a6ce88e6933dd2370cb149d))
* **api:** update via SDK Studio ([937feb3](https://github.com/tractorbeamai/tractorbeam-python/commit/937feb35527377cf7dade1e2470fa697f98b9c71))
* **api:** update via SDK Studio ([3b3c3e8](https://github.com/tractorbeamai/tractorbeam-python/commit/3b3c3e8e29dc00dbab74601fa61c481df3461e01))
* **api:** update via SDK Studio ([1d9ccd9](https://github.com/tractorbeamai/tractorbeam-python/commit/1d9ccd98dc06d453f1e2cbbce4d0e7377f229472))
* **api:** update via SDK Studio ([44107b7](https://github.com/tractorbeamai/tractorbeam-python/commit/44107b73fbade235b528daa6c0311771c23debc4))


### Chores

* go live ([#1](https://github.com/tractorbeamai/tractorbeam-python/issues/1)) ([03ba10a](https://github.com/tractorbeamai/tractorbeam-python/commit/03ba10a09a18eccb12cdd6beb8a1adc5d38f5504))
* **internal:** bump pydantic dependency ([1401220](https://github.com/tractorbeamai/tractorbeam-python/commit/1401220c89eff07db652618b3fc8e83e66016921))
* **internal:** codegen related update ([8c3e822](https://github.com/tractorbeamai/tractorbeam-python/commit/8c3e82247d96154c4a7e055cf8edb75748393f3a))
* **internal:** codegen related update ([2447901](https://github.com/tractorbeamai/tractorbeam-python/commit/244790147eb1d70924fdad9aeb011d8853049646))
* **internal:** codegen related update ([ecebe86](https://github.com/tractorbeamai/tractorbeam-python/commit/ecebe86dfabec9d0169b1b354ae0802e1dcb0ca8))
* **internal:** codegen related update ([f255707](https://github.com/tractorbeamai/tractorbeam-python/commit/f255707d0dcb507bae105402dbdceae341c06305))
* **internal:** codegen related update ([736097f](https://github.com/tractorbeamai/tractorbeam-python/commit/736097fc9df6a1a4cfbcf065268ba0be7cce04a4))
* **internal:** updated imports ([9da599d](https://github.com/tractorbeamai/tractorbeam-python/commit/9da599dbc7d425cbb28a12b4d709f61f447b7b5d))
* make the `Omit` type public ([0b748c9](https://github.com/tractorbeamai/tractorbeam-python/commit/0b748c9b4890395ff8354fe06b9661d407979840))
* update SDK settings ([#3](https://github.com/tractorbeamai/tractorbeam-python/issues/3)) ([6d9e3e3](https://github.com/tractorbeamai/tractorbeam-python/commit/6d9e3e359102eca204a661e00e01a3766450e1c1))


### Documentation

* **readme:** fix http client proxies example ([d4bb619](https://github.com/tractorbeamai/tractorbeam-python/commit/d4bb619b1cc19e1bf902cbea3627435e1b5b7edf))
