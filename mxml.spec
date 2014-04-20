Summary:      Miniature XML development library
Name:         mxml
Version:      2.8
Release:      1%{?dist}
License:      LGPLv2+
Group:        System Environment/Libraries
URL:          http://www.msweet.org/blog.php?L+Z3
Source0:      https://www.msweet.org/files/project3/mxml-2.8.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# This is requires because we patch configure.in.
BuildRequires: autoconf

%description
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
non-standard libraries.

%package devel
Summary:  Libraries, includes, etc to develop mxml applications
Group:    Development/Libraries
Requires: mxml = %{version}-%{release}
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop mxml
applications.

%prep
%setup -q

%build
# Run autoconf since we patched configure.in.
autoconf
%configure --enable-shared
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make BUILDROOT=%{buildroot} install

# Configuring with --disable-static doesn't work, so let's just delete
# the .a file by hand.
rm %{buildroot}%{_libdir}/libmxml.a

# remove extra docs
rm -rf %{buildroot}%{_datadir}/doc/mxml/

# remove rendered man pages
rm -f %{buildroot}%{_datadir}/man/cat*/*


%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/*
%{_libdir}/libmxml.so.*

%files devel
%defattr(-,root,root,-)
%doc CHANGES doc/*.html doc/*.gif
%{_includedir}/*.h
%{_libdir}/libmxml.so
%{_mandir}/*/*
%{_libdir}/pkgconfig/mxml.pc

%changelog
* Sun Apr 20 2014 @42wim
- Taken from fedora git

* Sun Apr 06 2014 Brendan Jones <brendan.jones.it@gmail.com> 2.8-1
- Update to 2.8

* Tue Dec 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 2.6-1
- Update to 2.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 28 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.5-5
- Fix typo in the .pc file (RHBZ#503628). Patch by Robert Szalai

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-2
- fix license tag

* Tue Jul 08 2008 Anthony Green <green@redhat.com> 2.5
- Upgrade source.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.2-8
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.2.2-7
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 2.2.2-6
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> 2.2.2-5.1
- Rebuild.

* Mon Sep  4 2006 Anthony Green <green@redhat.com> 2.2.2-5
- devel package must Require pkgconfig.

* Wed Jul 19 2006 Anthony Green <green@redhat.com> 2.2.2-4
- Fix /usr/share references.

* Sat Jul 15 2006 Anthony Green <green@redhat.com> 2.2.2-3
- Fix /usr/lib reference when deleting libmxml.a.

* Sat Jul 15 2006 Anthony Green <green@redhat.com> 2.2.2-2
- Fix License (LGPL, not GPL).
- Move programming documentation to devel package.
- Build shared library, and no static library.
- Add %%post(un).
- Remove rpath with mxml-no-rpath.patch.
- First Fedora Extras build.

* Fri Sep 23 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.2-1
- updated to 2.2.2 (zynaddsubfx needs 2.2 at least)
* Mon Dec 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanup
* Wed Aug  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0-1
- initial build.


