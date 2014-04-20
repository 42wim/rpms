Name:           libmnl
Version:        1.0.3
Release:        4%{?dist}
Summary:        Minimalistic Netlink Library
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://netfilter.org/projects/libmnl/index.html
Source0:        http://netfilter.org/projects/libmnl/files/libmnl-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong. 
This library aims to provide simple helpers that allows you to re-use code
and to avoid re-inventing the wheel.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use code
and to avoid re-inventing the wheel.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu May 02 2013 @42wim
- update to 1.0.3
* Thu Dec 30 2010 Paul P. Komkoff <i@stingr.net> 1.0.0-1
- initial import.
