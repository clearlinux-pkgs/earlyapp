#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : earlyapp
Version  : 1.0.16
Release  : 19
URL      : https://github.com/intel/earlyapp/archive/v1.0.16.tar.gz
Source0  : https://github.com/intel/earlyapp/archive/v1.0.16.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: earlyapp-bin = %{version}-%{release}
Requires: earlyapp-config = %{version}-%{release}
Requires: earlyapp-data = %{version}-%{release}
Requires: earlyapp-license = %{version}-%{release}
Requires: earlyapp-services = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libmfxhw64)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(wayland-client)

%description
# Early App
## Introduction
This software is a testing application that runs on Clear Linux to verify
cold boot to audio, video and RVC (Reverse View Camera) functionalities on Intel platforms.

%package bin
Summary: bin components for the earlyapp package.
Group: Binaries
Requires: earlyapp-data = %{version}-%{release}
Requires: earlyapp-config = %{version}-%{release}
Requires: earlyapp-license = %{version}-%{release}
Requires: earlyapp-services = %{version}-%{release}

%description bin
bin components for the earlyapp package.


%package config
Summary: config components for the earlyapp package.
Group: Default

%description config
config components for the earlyapp package.


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
%setup -q -n earlyapp-1.0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551764835
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1551764835
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
/usr/bin/earlyapp-fastboot

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/50-earlyapp.rules

%files data
%defattr(-,root,root,-)
/usr/share/earlyapp/beep.wav
/usr/share/earlyapp/clear_fb.fb
/usr/share/earlyapp/early_audio.sh
/usr/share/earlyapp/jingle.wav
/usr/share/earlyapp/kpi_gpio.sh
/usr/share/earlyapp/mem_hot_add.sh
/usr/share/earlyapp/preload.txt
/usr/share/earlyapp/splash_video.h264
/usr/share/earlyapp/splash_video.mp4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/earlyapp/LICENSE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/early-audio.service
/usr/lib/systemd/system/early-audio_resume.service
/usr/lib/systemd/system/earlyapp-setup-aud.service
/usr/lib/systemd/system/earlyapp-setup-cbc.service
/usr/lib/systemd/system/earlyapp-setup-ipu.service
/usr/lib/systemd/system/earlyapp-setup-render.service
/usr/lib/systemd/system/earlyapp-setup_gpnative.service
/usr/lib/systemd/system/earlyapp-setup_gst.service
/usr/lib/systemd/system/earlyapp.service
/usr/lib/systemd/system/earlyapp.slice
/usr/lib/systemd/system/earlyapp.target
/usr/lib/systemd/system/earlyapp_gpnative.service
/usr/lib/systemd/system/earlyapp_gpnative.target
/usr/lib/systemd/system/earlyapp_gst.service
/usr/lib/systemd/system/earlyapp_gst.target
/usr/lib/systemd/system/earlyapp_resume.service
/usr/lib/systemd/system/earlyapp_suspend.service
/usr/lib/systemd/system/ias-earlyapp-setup.service
/usr/lib/systemd/system/ias-earlyapp-wait.service
/usr/lib/systemd/system/ias-earlyapp.service
/usr/lib/systemd/system/mem_hot_add.service
/usr/lib/systemd/system/simple-egl.service
/usr/lib/systemd/system/simple-egl_resume.service
