#sbs-git:slp/pkgs/a/alsa-utils alsa-utils 1.0.21 7b8a27d87cefc0e56d80383e61a0385e88cd90fd

Name:       alsa-utils
Summary:    Advanced Linux Sound Architecture (ALSA) utilities
Version: 1.0.21
Release:    1
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
    --disable-alsatest

make %{?jobs:-j%jobs}

exit

%install
rm -rf %{buildroot}
%make_install

%remove_docs

%files
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/alsa/*
%{_datadir}/sounds/*

