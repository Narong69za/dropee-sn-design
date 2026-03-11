# CHANGELOG

All notable changes to this project will be documented in this file.

---

## [1.1.1] - 2026-03-11

### Added
- Added `dropee_api.py` centralized API handler
- Prepared system structure for debugging API errors

### Improved
- Improved engine logging visibility
- Better API response inspection for troubleshooting

### Fixed
- Initial handling for potential JSON parsing issues

### Files Updated
- core/engine.py
- modules/dropee_api.py

---

## [1.1.0] - 2026-03-11

### Added
- Initial Dropee Engine system
- Account loader module
- Task / Tap / Reward execution cycle

### Files
- core/engine.py
- modules/tasks.py
- modules/tap.py
- modules/rewards.py
