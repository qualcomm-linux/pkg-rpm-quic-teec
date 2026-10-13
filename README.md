# pkg-rpm-quic-teec

RPM packaging for [`quic/quic-teec`](https://github.com/qualcomm/quic-teec)
— QCOM-TEE Library provides an interface for communication to the Qualcomm Trusted Execution Environment (QTEE)
via the QCOM-TEE driver registered with the Linux TEE subsystem. QCOM-TEE Library supports Object-based IPC
with QTEE for user-space clients via the `TEE_IOC_OBJECT_INVOKE` IOCTL from the Linux TEE subsystem.

This repo builds and publishes the `quic-teec` RPM via the shared
[`qualcomm-linux/qcom-rpm-utils`](https://github.com/qualcomm-linux/qcom-rpm-utils)
reusable workflows — it follows the same one-package-per-repo template used
across `qualcomm-linux/pkg-rpm-*`.

## Branches

Following the Fedora/CentOS **dist-git** convention, each distro stream gets its
own branch, and the packaging files live at the branch root:

| Branch | Stream | Contents |
|---|---|---|
| `main` | — | Template docs, onboarding guide, community files. Nothing is built here. |
| **`c10s`** | CentOS 10 Stream | **This branch.** `quic-teec.spec` + `sources` + workflows. |

Full onboarding guide, configuration reference, and troubleshooting live on
[`main`](../../tree/main) — see its `README.md` and `docs/workflows.md`.

## Installation Instructions

```
sudo rpm -i quic-teec-x.aarch64.rpm
sudo rpm -i quic-teec-devel-x.aarch64.rpm
```

## Getting in Contact

How to contact maintainers. E.g. GitHub Issues, GitHub Discussions could be indicated for many cases. However a mail list or list of Maintainer e-mails could be shared for other types of discussions. E.g.

* [Report an Issue on GitHub](../../issues)
* [Open a Discussion on GitHub](../../discussions)

## License

pkg-rpm-quic-teec is licensed under the [BSD-3-clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE.txt](LICENSE.txt) for the full license text.
