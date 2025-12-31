Name:           howdy-selinux
Version:        3.0.0
Release:        1%{?dist}
Summary:        SELinux policy module for howdy (pam_howdy)

# The entire source code is GPL-3.0-or-later except:
# howdy/src/recorders/v4l2.py which is GPL-2.0-or-later OR BSD-3-Clause.
License:        MIT AND (GPL-2.0-or-later OR BSD-3-Clause)
BuildArch:      noarch
URL:            %{forgeurl}
Source0:        howdy.te

BuildRequires:  selinux-policy-devel

Requires:       policycoreutils
Requires:       selinux-policy-targeted

%global modulename howdy
%global moduletype targeted

%description
SELinux policy module to allow pam_howdy (running under local_login_t).

This package installs and loads an SELinux policy module.

%prep
%setup -q -c -T
cp %{SOURCE0} %{modulename}.te

%build
checkmodule -M -m -o %{modulename}.mod %{modulename}.te
semodule_package -o %{modulename}.pp -m %{modulename}.mod

%install
install -D -m 0644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{modulename}.pp

%files
%license
%doc
%{_datadir}/selinux/packages/%{modulename}.pp

%changelog
* Wed Dec 31 2025 Koji AGAWA <me@atty303.ninja> - 3.0.0-1
- Initial SELinux policy module for howdy
