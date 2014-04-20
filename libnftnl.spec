Name:           libnftnl
Version:        1.0.1
Release:        1%{?dist}
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl

License:        GPLv2+
URL:            http://netfilter.org/projects/libnftnl/
Source0:        http://netfilter.org/projects/libnftnl/files/libnftnl-1.0.1.tar.bz2

#BuildRequires:  autogen
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libmnl-devel
BuildRequires:  jansson-devel

# replace old libnftables package
Provides: libnftables = %{version}-%{release}
Obsoletes: libnftables < 0-0.6

%description
A library for low-level interaction with nftables Netlink's API over libmnl.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
# replace old libnftables-devel package
Provides: libnftables-devel = %{version}-%{release}
Obsoletes: libnftables-devel < 0-0.6

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libnftnl-%{version}

%build
%configure --disable-static --disable-silent-rules --with-json-parsing --with-xml-parsing
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/libnft*.so
%{_libdir}/pkgconfig/libnftnl.pc
%{_includedir}/libnftnl

%changelog
* Sun Apr 20 2014 @42wim
- Taken from fedora git

* Sun Mar 30 2014 Kevin Fenzi <kevin@scrye.com> 1.0.0-1.20140330git
- Update to 20140330 snapshot
- Sync version to be a post 1.0.0 snapshot

* Wed Mar 26 2014 Kevin Fenzi <kevin@scrye.com> 0-0.10.20140326git
- Update to 20140326 snapshot

* Fri Mar 07 2014 Kevin Fenzi <kevin@scrye.com> 0-0.9.20140307git
- Update to 20140307 snapshot

* Sat Jan 25 2014 Kevin Fenzi <kevin@scrye.com> 0-0.8.20140125git
- Update to 20140125

* Thu Jan 23 2014 Kevin Fenzi <kevin@scrye.com> 0-0.7.20140122git
- Add obsoletes/provides to devel subpackage as well. 

* Wed Jan 22 2014 Kevin Fenzi <kevin@scrye.com> 0-0.6.20140122git
- Renamed libnftnl
- Update to 20140122 snapshot.

* Sat Jan 18 2014 Kevin Fenzi <kevin@scrye.com> 0-0.5.20140118git
- Update to 20140118 snapshot.

* Sat Jan 11 2014 Kevin Fenzi <kevin@scrye.com> 0-0.4.20140111git
- Update to 20140111 snapshot. 
- Enable xml (some tests stll fail, but it otherwise builds ok)

* Mon Dec 02 2013 Kevin Fenzi <kevin@scrye.com> 0-0.3.20131202git
- Update to 20131202 snapshot, switch to upstream snapshot repo instead of git checkouts. 

* Mon Dec 02 2013 Kevin Fenzi <kevin@scrye.com> 0-0.2
- Fixes from review. 

* Sat Nov 30 2013 Kevin Fenzi <kevin@scrye.com> 0-0.1
- initial version for Fedora review
