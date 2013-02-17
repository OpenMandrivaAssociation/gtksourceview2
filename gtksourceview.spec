%define api_version 2.0
%define lib_major 0
%define libname %mklibname %{name}- %{api_version} %{lib_major}
%define libnamedev %mklibname -d %{name}- %{api_version}


Summary:	Source code viewing library
Name:		gtksourceview
Version:	2.11.2
Release:	3
License:	GPLv2+
Group:		Editors
URL:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	gtk-doc
BuildRequires:	intltool

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libname}
Summary:	Source code viewing library
Group:		Editors
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
Provides:	libgtksourceview0 = %{version}-%{release}
Obsoletes:	libgtksourceview0 < 2.10.5-7
Provides:	libgtksourceview1.0 = %{version}-%{release}
Obsoletes:	libgtksourceview1.0 < 2.10.5-7

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libnamedev}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d gtksourceview- 2.0 0} < 2.10.5-7

%description -n %{libnamedev}
GtkSourceView development files.

%prep
%setup -q

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std

%find_lang %{name}-%{api_version}

%files -f %{name}-%{api_version}.lang
%doc AUTHORS NEWS README
%{_datadir}/gtksourceview-%{api_version}

%files -n %{libname}
%{_libdir}/libgtksourceview-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%doc %{_datadir}/gtk-doc/html/gtksourceview-2.0
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*


%changelog
* Wed Mar 28 2012 Götz Waschk <waschk@mandriva.org> 2.10.5-6mdv2012.0
+ Revision: 787940
- rebuild

* Thu Dec 15 2011 Götz Waschk <waschk@mandriva.org> 2.10.5-5
+ Revision: 741508
- remove libtool archive

* Fri Dec 02 2011 Andrey Bondrov <abondrov@mandriva.org> 2.10.5-4
+ Revision: 737231
- Rebuild to fix problems caused by Matthew Dawkins (.la files issue)

* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 2.10.5-3
+ Revision: 700859
- rebuild

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.10.5-2
+ Revision: 664957
- mass rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.10.5-1mdv2011.0
+ Revision: 581802
- new stable version 2.10.5

* Mon Sep 20 2010 Götz Waschk <waschk@mandriva.org> 2.11.2-2mdv2011.0
+ Revision: 579958
- rebuild for new g-i

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.11.2-1mdv2011.0
+ Revision: 563496
- update build deps
- new version
- add introspection support

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.10.4-1mdv2011.0
+ Revision: 550812
- update to new version 2.10.4

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.10.1-2mdv2010.1
+ Revision: 540346
- rebuild so that shared libraries are properly stripped again

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2010.1
+ Revision: 538922
- update to new version 2.10.1

* Sun Mar 28 2010 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2010.1
+ Revision: 528497
- update to new version 2.10.0

* Wed Mar 17 2010 Götz Waschk <waschk@mandriva.org> 2.9.9-1mdv2010.1
+ Revision: 523305
- update to new version 2.9.9

* Mon Mar 01 2010 Götz Waschk <waschk@mandriva.org> 2.9.8-1mdv2010.1
+ Revision: 513136
- update to new version 2.9.8

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 2.9.7-1mdv2010.1
+ Revision: 509802
- update to new version 2.9.7

* Mon Jan 25 2010 Götz Waschk <waschk@mandriva.org> 2.9.5-1mdv2010.1
+ Revision: 496484
- update to new version 2.9.5

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 2.9.4-1mdv2010.1
+ Revision: 490117
- update to new version 2.9.4

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.9.3-1mdv2010.1
+ Revision: 475488
- update build deps
- update to new version 2.9.3

* Mon Sep 28 2009 Götz Waschk <waschk@mandriva.org> 2.8.1-1mdv2010.0
+ Revision: 450709
- update to new version 2.8.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.8.0-1mdv2010.0
+ Revision: 446726
- update to new version 2.8.0

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 2.7.5-1mdv2010.0
+ Revision: 440951
- update to new version 2.7.5

* Sun Aug 23 2009 Götz Waschk <waschk@mandriva.org> 2.7.4-1mdv2010.0
+ Revision: 420183
- update to new version 2.7.4

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 2.7.3-1mdv2010.0
+ Revision: 401390
- update to new version 2.7.3

* Sun Jul 19 2009 Götz Waschk <waschk@mandriva.org> 2.7.2-1mdv2010.0
+ Revision: 397895
- update to new version 2.7.2

* Tue May 26 2009 Götz Waschk <waschk@mandriva.org> 2.7.1-1mdv2010.0
+ Revision: 379942
- update to new version 2.7.1

* Sat May 16 2009 Götz Waschk <waschk@mandriva.org> 2.6.2-1mdv2010.0
+ Revision: 376420
- new version
- drop patch

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.6.1-1mdv2009.1
+ Revision: 366973
- update to new version 2.6.1

* Sun Mar 15 2009 Götz Waschk <waschk@mandriva.org> 2.6.0-1mdv2009.1
+ Revision: 355375
- update to new version 2.6.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.5.6-1mdv2009.1
+ Revision: 347284
- update to new version 2.5.6

* Sun Feb 15 2009 Götz Waschk <waschk@mandriva.org> 2.5.5-1mdv2009.1
+ Revision: 340569
- update to new version 2.5.5

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 2.5.4-1mdv2009.1
+ Revision: 336732
- update to new version 2.5.4

* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 2.5.3-1mdv2009.1
+ Revision: 331392
- update to new version 2.5.3

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 2.5.2-1mdv2009.1
+ Revision: 325233
- update to new version 2.5.2

* Sat Dec 27 2008 Götz Waschk <waschk@mandriva.org> 2.5.1-1mdv2009.1
+ Revision: 319938
- new version
- fix build

* Fri Nov 07 2008 Götz Waschk <waschk@mandriva.org> 2.4.1-2mdv2009.1
+ Revision: 300852
- rebuild for new libxcb

* Sat Nov 01 2008 Götz Waschk <waschk@mandriva.org> 2.4.1-1mdv2009.1
+ Revision: 299158
- update to new version 2.4.1

* Sat Sep 20 2008 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2009.0
+ Revision: 286080
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.3.3-1mdv2009.0
+ Revision: 282762
- new version

* Sun Aug 31 2008 Götz Waschk <waschk@mandriva.org> 2.3.2-1mdv2009.0
+ Revision: 277896
- new version

* Mon Aug 11 2008 Götz Waschk <waschk@mandriva.org> 2.3.1-1mdv2009.0
+ Revision: 270640
- new version

* Sat Aug 09 2008 Götz Waschk <waschk@mandriva.org> 2.3.0-1mdv2009.0
+ Revision: 270093
- new version
- update license
- don't depend on gnomeprint anymore

* Mon Jun 23 2008 Götz Waschk <waschk@mandriva.org> 2.2.2-1mdv2009.0
+ Revision: 227969
- new version

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2009.0
+ Revision: 192472
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2008.1
+ Revision: 183387
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.1.3-1mdv2008.1
+ Revision: 174978
- new version

* Tue Feb 05 2008 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2008.1
+ Revision: 162620
- new version

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdv2008.1
+ Revision: 159723
- new version

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 2.1.0-1mdv2008.1
+ Revision: 151726
- fix buildrequires
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Götz Waschk <waschk@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 113311
- new version

* Wed Oct 17 2007 Götz Waschk <waschk@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 99555
- new version

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdv2008.0
+ Revision: 88995
- new version
- update file list

* Mon Sep 10 2007 Götz Waschk <waschk@mandriva.org> 1.90.5-1mdv2008.0
+ Revision: 84189
- new version

* Thu Aug 30 2007 Götz Waschk <waschk@mandriva.org> 1.90.4-2mdv2008.0
+ Revision: 75310
- remove wrong obsoletes

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 1.90.4-1mdv2008.0
+ Revision: 72490
- new version
- new devel name

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 1.90.3-1mdv2008.0
+ Revision: 57377
- new version

* Wed Jul 04 2007 Götz Waschk <waschk@mandriva.org> 1.90.2-1mdv2008.0
+ Revision: 47927
- new version
- update file list

* Tue Jun 19 2007 Götz Waschk <waschk@mandriva.org> 1.90.1-1mdv2008.0
+ Revision: 41284
- new version
- new version
- new API version

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags


* Sun Mar 11 2007 Götz Waschk <waschk@mandriva.org> 1.8.5-1mdv2007.1
+ Revision: 141416
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Mon Feb 12 2007 Götz Waschk <waschk@mandriva.org> 1.8.4-1mdv2007.1
+ Revision: 120047
- new version

* Tue Jan 30 2007 Götz Waschk <waschk@mandriva.org> 1.8.3-1mdv2007.1
+ Revision: 115466
- new version

* Thu Dec 14 2006 Götz Waschk <waschk@mandriva.org> 1.8.2-1mdv2007.1
+ Revision: 96755
- new version

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 1.8.1-3mdv2007.1
+ Revision: 63817
- rebuild
- rebuild
- Import gtksourceview

* Wed Oct 04 2006 Götz Waschk <waschk@mandriva.org> 1.8.1-1mdv2007.0
- New version 1.8.1

* Tue Sep 05 2006 Götz Waschk <waschk@mandriva.org> 1.8.0-1mdv2007.0
- New release 1.8.0

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 1.7.2-1mdv2007.0
- New release 1.7.2

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 1.7.1-1mdk
- New release 1.7.1

* Wed Apr 19 2006 Frederic Crozat <fcrozat@mandriva.com> 1.6.1-1mdk
- Release 1.6.1

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 1.4.2-2mdk
- Use mkrel

* Fri Oct 07 2005 Frederic Crozat <fcrozat@mandriva.com> 1.4.2-1mdk
- Release 1.4.2

* Thu Jul 14 2005 G�tz Waschk <waschk@mandriva.org> 1.2.1-1mdk
- New release 1.2.1

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 1.2.0-1mdk 
- Release 1.2.0 (based on G�tz Waschk package)
- Remove patch0 (merged upstream)

* Thu Mar 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.1-2mdk
- Fix upgrade from MDK 10.1

* Wed Nov 10 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.1.1-1mdk
- New release 1.1.1
- Enable libtoolize
- Patch0 (Fedora): Fix problem with backspace to delete partial characters

* Fri Apr 23 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.0.1-2mdk
- fix buildrequires

* Tue Apr 20 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.0.1-1mdk
- new version

* Wed Apr 07 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.0-1mdk
- Release 1.0.0 (with G�tz help)
- requires new gtk

