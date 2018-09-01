%global commit e8effadebc349d38f7b8a2c190baa72ebf74b6fe
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180825

%global kodi_addon pvr.iptvsimple
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        3.5.3
Release:        1%{?dist}
Summary:        Simple IPTV PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz
# Use external rapidxml library
Patch0:         %{name}-3.4.2-use_external_rapidxml.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
BuildRequires:  rapidxml-devel
BuildRequires:  zlib-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64 aarch64

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Drop bundled rapidxml library
rm -r lib/rapidxml/


%build
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.3-1
- Update to 3.5.3
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.2-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:2.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.14-1
- Update to 2.4.14

* Wed Apr 26 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.11-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.12.14-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.5-1
- Initial RPM release
