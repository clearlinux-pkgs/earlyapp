#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : earlyapp
Version  : 0.9.12
Release  : 1
URL      : https://github.com/intel/earlyapp/archive/v0.9.12.tar.gz
Source0  : https://github.com/intel/earlyapp/archive/v0.9.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: earlyapp-bin = %{version}-%{release}
Requires: earlyapp-data = %{version}-%{release}
Requires: earlyapp-license = %{version}-%{release}
Requires: earlyapp-services = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(gstreamer-1.0)

%description
# Early App
## Introduction
This software is a testing application that runs on Clear Linux to verify
cold boot to audio, video and RVC (Reverse View Camera) functionalities on Intel platforms.

%package bin
Summary: bin components for the earlyapp package.
Group: Binaries
Requires: earlyapp-data = %{version}-%{release}
Requires: earlyapp-license = %{version}-%{release}
Requires: earlyapp-services = %{version}-%{release}

%description bin
bin components for the earlyapp package.


%package data
Summary: data components for the earlyapp package.
Group: Data

%description data
data components for the earlyapp package.


%package license
Summary: license components for the earlyapp package.
Group: Default

%description license
license components for the earlyapp package.


%package services
Summary: services components for the earlyapp package.
Group: Systemd services

%description services
services components for the earlyapp package.


%prep
%setup -q -n earlyapp-0.9.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541744844
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1541744844
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/earlyapp
cp LICENSE %{buildroot}/usr/share/package-licenses/earlyapp/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/earlyapp

%files data
%defattr(-,root,root,-)
/usr/share/earlyapp/beep.wav
/usr/share/earlyapp/clear_fb.fb
/usr/share/earlyapp/jingle.wav
/usr/share/earlyapp/kpi_gpio.sh
/usr/share/earlyapp/splash_video.mp4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/earlyapp/LICENSE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/cbc_attach.service
/usr/lib/systemd/system/earlyapp.service
/usr/lib/systemd/system/earlyapp.slice
/usr/lib/systemd/system/earlyapp.target
/usr/lib/systemd/system/earlyapp_resume.service
/usr/lib/systemd/system/fb_splash.service
/usr/lib/systemd/system/glmark2.service
/usr/lib/systemd/system/glmark2_resume.service
/usr/lib/systemd/system/ias-earlyapp.service
/usr/lib/systemd/system/ias-pre.service
