%global srcname april-asr
%global commit 3308e68442664552de593957cad0fa443ea183dd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230903

Name:           april-asr
Version:        0~git%{commitdate}.%{shortcommit}
Release:        %autorelease
Summary:        Minimal library for offline streaming speech-to-text applications
	
License:        GPL-2.0-or-later
URL:            https://github.com/abb128/april-asr
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

Patch0:         april-asr-0-pkgconfig-fix.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  onnxruntime-devel

%description
%{summary}.

%package devel
Requires:      %{name}%{?_isa} = %{version}-%{release}
 
Summary:       Development files for %{name}
 
%description devel
%{summary}.


%prep
%autosetup -n %{srcname}-%{commit}

%build
%cmake \
    -D CMAKE_INSTALL_LIBDIR=/usr/lib64/ \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D LINUX_PORTABLE=OFF \
    -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
%{_libdir}/libaprilasr.so.2023{,.*}
 
%files devel
%{_includedir}/april-asr/*
%{_libdir}/libaprilasr.so
%{_libdir}/pkgconfig/april-asr.pc

%changelog
%autochangelog