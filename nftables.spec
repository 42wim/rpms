Name:           nftables
Version:        0.2
Release:        1%{?dist}
Summary:        Netfilter Tables userspace utillites

License:        GPLv2
URL:            http://netfilter.org/projects/nftables/
Source0:        http://ftp.netfilter.org/pub/nftables/snapshot/nftables-%{version}.tar.bz2

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: flex
BuildRequires: bison
BuildRequires: libmnl-devel
BuildRequires: gmp-devel
BuildRequires: readline-devel
BuildRequires: libnftnl-devel
BuildRequires: docbook2X
BuildRequires: docbook-dtds

%description
Netfilter Tables userspace utilities.

%prep
%setup -q -n nftables-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man8/nft*

%files
%doc COPYING TODO
%config(noreplace) %{_sysconfdir}/nftables/
%{_sbindir}/nft
%{_mandir}/man8/nft*

%changelog
* Sun Apr 20 2014 @42wim
- Taken from fedora git

* Sun Mar 30 2014 Kevin Fenzi <kevin@scrye.com> 0.100-1.20140330git
- Update to 20140330 snapshot
- Sync versions to be post 0.100 release.

* Wed Mar 26 2014 Kevin Fenzi <kevin@scrye.com> 0-0.7.20140326git
- Update to 20140326 snapshot
- Fix permissions on man pages. 

* Mon Mar 24 2014 Kevin Fenzi <kevin@scrye.com> 0-0.6.20140324git
- Update to 20140324 snapshot

* Fri Mar 07 2014 Kevin Fenzi <kevin@scrye.com> 0-0.5.20140307git
- Update to 20140307

* Sat Jan 25 2014 Kevin Fenzi <kevin@scrye.com> 0-0.4.20140125git
- Update to 20140125 snapshot

* Sat Jan 18 2014 Kevin Fenzi <kevin@scrye.com> 0-0.3.20140118git
- Update to 20140118 snapshot
- Fixed License tag to be correct
- Fixed changelog
- nft scripts now use full path for nft
- Fixed man page building
- Dropped unneeded rm in install
- Patched build to not be silent. 

* Tue Dec 03 2013 Kevin Fenzi <kevin@scrye.com> 0-0.2.20131202git
- Use upstream snapshots for source.
- Use 0 for version. 

* Sat Nov 30 2013 Kevin Fenzi <kevin@scrye.com> 0-0.1
- initial version for Fedora review
