Name:		quic-teec
Version:	1.0.1
Release:	1%{?dist}
Summary:	Qualcomm qcomtee userspace library

License:	BSD-3-Clause
URL:		https://github.com/quic/quic-teec
Source0:	https://github.com/quic/quic-teec/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	qcbor-devel

%description
QCOM-TEE (libqcomtee) is a user-space C library that enables applications to
communicate with Qualcomm's Trusted Execution Environment (QTEE) via the
Linux TEE subsystem using object-based IPC.

This package contains the shared library libqcomtee.so.


%package devel
Summary: Development files for the qcomtee library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files needed to build and link to the libqcomtee library.


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libqcomtee.so.*

%files devel
%{_libdir}/libqcomtee.so
%{_includedir}/qcomtee_*.h
%{_libdir}/pkgconfig/qcomtee.pc


%changelog
* Wed Sep 02 2026 Abhinaba Rakshit <abhinaba.rakshit@oss.qualcomm.com> - 1.0.1-1
- Initial RPM package with upstream v1.0.1
