<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# Package branch — CentOS 10 Stream (`c10s`)

**This is the branch you work on.** It holds the `quic-teec.spec` RPM's spec file and
`sources` pointer, plus the CI workflows that build and publish them.

## quic-teec RPM package

This RPM packages [`quic/quic-teec`](https://github.com/quic/quic-teec)
— QCOM-TEE Library provides an interface for communication to the Qualcomm Trusted Execution Environment (QTEE)
via the QCOM-TEE driver registered with the Linux TEE subsystem. QCOM-TEE Library supports Object-based IPC
with QTEE for user-space clients via the `TEE_IOC_OBJECT_INVOKE` IOCTL from the Linux TEE subsystem.

## Package contents

| File | Purpose |
|---|---|
| [`quic-teec.spec`](quic-teec.spec) | RPM spec for `quic-teec.spec`. Builds via autotools (`cmake` + `%cmake_build`), installs the `libqcomtee` shared library generated inline in `%install`. |
| [`sources`](sources) | dist-git checksum pointer for the upstream `v1.0.1` release tarball (SHA512). The tarball itself is never committed — see [`docs/workflows.md`](docs/workflows.md) for the lookaside-cache model. |
| [`.github/workflows/`](.github/workflows) | build-on-pr.yml, pkg-release.yml CI workflow files. |

## Getting started

### Update the version

Two edits, every time:

1. Bump `Version:` in [`quic-teec.spec`](quic-teec.spec) (and the
   `Source0:` URL if the upstream release layout changed).
2. Recompute the checksum:
   ```bash
   sha512sum --tag quic-teec-<newversion>.tar.gz > sources
   ```

Commit both, open a PR against this branch, merge, then run **Release**. The
first release fetches the new upstream tarball, verifies it, and caches it back
automatically.

### Open a PR

`build-on-pr` fetches the tarball (from the lookaside cache, or from the spec's
`Source` URL on a cache miss), verifies the checksum, and builds the RPM.
Download it from the run's **Artifacts**.

### Release

**Actions → Release → Run workflow**, selecting this branch. A reviewer
approves the `pkg-release-approval` gate, then the RPM publishes to
Artifactory.
