%global commit 2a649d7e21b64c4fa4a8b14c2cc139261eebc7e8
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170817

%global kodi_addon pvr.iptvsimple
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        2.4.14
Release:        1%{?dist}
Summary:        Kodi's IPTV Simple client addon

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# Use external rapidxml library
Patch0:         %{name}-2.4.11-use_external_rapidxml.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
BuildRequires:  rapidxml-devel
BuildRequires:  zlib-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
Kodi PVR addon for IPTV support, with M3U playlists, streaming of live TV for
multicast/unicast sources, listening to radio channels and EPG.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Drop bundled rapidxml library
rm -r lib/rapidxml/

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Tue Feb 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.14-1
- Update to 2.4.14

* Wed Apr 26 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.11-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.12.14-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.5-1
- Initial RPM release
