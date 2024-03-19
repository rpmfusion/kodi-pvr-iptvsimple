%global kodi_addon pvr.iptvsimple
%global kodi_version 21
%global kodi_codename Omega

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        21.8.2
Release:        1%{?dist}
Summary:        Simple IPTV PVR for Kodi

License:        GPL-2.0-or-later
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  xz-devel
Requires:       kodi >= %{kodi_version}
Requires:       kodi-inputstream-adaptive%{?_isa} >= %{kodi_version}
# TODO: uncomment once kodi-inputstream-ffmpegdirect is packaged (see RFBZ #6387)
# Requires:       kodi-inputstream-ffmpegdirect%%{?_isa} >= %%{kodi_version}
Requires:       kodi-inputstream-rtmp%{?_isa} >= %{kodi_version}
ExcludeArch:    %{power64}

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename} -p0


%build
%cmake
%cmake_build


%install
%cmake_install

# Install AppData file
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Thu Mar 14 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:21.8.2-1
- Update to 21.8.2

* Sat Feb 17 2024 Leigh Scott <leigh123linux@gmail.com> - 1:20.13.0-1
- Update to 20.13.0

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:20.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 25 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:20.11.0-1
- Update to 20.11.0

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:20.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 19 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:20.10.1-1
- Update to 20.10.1
- Fix Requires (RFBZ #6656)

* Mon Mar 27 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:20.9.1-1
- Update to 20.9.1

* Sun Feb 12 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:20.8.0-1
- Update to 20.8.0

* Sun Feb 12 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:20.7.0-1
- Update to 20.7.0

* Sun Jan 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:20.6.1-1
- Update to 20.6.1
- Add AppStream metadata
- Switch to SPDX license identifiers

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:7.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:7.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:7.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.6.7-1
- Update to 7.6.7

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:7.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.3.0-1
- Update to 7.3.0

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.0.0-1
- Update to 7.0.0

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:6.3.0-1
- Update to 6.3.0 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.8.8-1
- Update to 3.8.8

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.3-2
- Enable arm build

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
