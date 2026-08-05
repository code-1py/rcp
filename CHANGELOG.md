# Changelog

## 1.0.3

### Added

- Added `authority` to `HTTPScope` for exposing the HTTP/3 `:authority` pseudo-header.
- Added optional `reason` field to `HTTPDisconnectEvent`.
- Exported additional public protocol type aliases:
  - `HTTPReceiveEvents`
  - `HTTPSendEvents`
  - `LifespanReceiveEvents`
  - `LifespanSendEvents`
  - `RCP`
  - `RCPVersions`
  - `RequestMethod`
  - `HTTPScheme`

### Changed

- Expanded the public API to expose protocol definitions intended for framework and server authors.

## 1.0.2

### Fixed

- Removed accidental inclusion of development environment files from package distributions.
- Fixed version inconsistencies between package metadata and internal version information.

### Changed

- Improved package release verification workflow.
- Added cleaner distribution checks before publishing releases.

## 1.0.0

### Added

- Initial RCP release
- HTTP/3 support
- Lifespan protocol
- Typed scopes
- Typed events