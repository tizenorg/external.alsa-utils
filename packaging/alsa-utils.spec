#sbs-git:slp/pkgs/a/alsa-utils alsa-utils 1.0.21 7b8a27d87cefc0e56d80383e61a0385e88cd90fd

Name:       alsa-utils
Summary:    Advanced Linux Sound Architecture (ALSA) utilities
Version:    1.0.24.3
Release:    0
Group:      Applications/Multimedia
License:    GPLv2+
URL:        http://www.alsa-project.org/
Source0:    ftp://ftp.alsa-project.org/pub/utils/alsa-utils-%{version}.tar.gz
BuildRequires:  libasound-devel


%description
This package contains command line utilities for the Advanced Linux Sound
Architecture (ALSA).



%package doc
Summary:    Man pages for alsa-utils
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Man pages for alsa-utils



%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static \
    --disable-nls \
    --disable-xmlto \
    --disable-alsamixer \
    --disable-alsatest \
    --disable-alsaconf \
    --with-udev-rules-dir=/usr/lib/udev/rules.d

make %{?jobs:-j%jobs}

exit

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
mkdir -p %{buildroot}/opt/usr/devel/usr/bin
mkdir -p %{buildroot}/opt/usr/devel/usr/sbin
cp COPYING %{buildroot}/usr/share/license/%{name}

%make_install

mv %{buildroot}/usr/bin/* %{buildroot}/opt/usr/devel/usr/bin
mv %{buildroot}/usr/sbin/* %{buildroot}/opt/usr/devel/usr/sbin

%remove_docs

%files
%manifest alsa-utils.manifest
/opt/usr/devel/usr/bin/*
/opt/usr/devel/usr/sbin/*
%{_datadir}/alsa/*
%ifarch %{arm}
%{_datadir}/sounds/*
%else
%exclude %{_datadir}/sounds/*
%endif
/usr/lib/udev/rules.d/90-alsa-restore.rules
/usr/share/license/%{name}
