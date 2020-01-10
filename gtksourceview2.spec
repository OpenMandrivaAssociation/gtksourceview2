%define url_ver %(echo %{version}|cut -d. -f1,2)

%define _disable_rebuild_configure 1
%define _disable_lto 1

%define api	2.0
%define major	0
%define libname %mklibname %{name}- %{api} %{major}
%define devname %mklibname -d %{name}- %{api}

Summary:	Source code viewing library
Name:		gtksourceview2
Version:	2.11.2
Release:	18
License:	GPLv2+
Group:		Editors
Url:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceview/%{url_ver}/gtksourceview-%{version}.tar.bz2
Patch1:		gtksourceview-2.11-fix-GCONST-def.patch
Patch2: 	gtksourceview-2.11-glib-unicode-constant.patch
Patch3:		gtksourceview-2.11-compile.patch
# The tests are seriously broken and violating just
# about every rule of -Werror sanity there is.
# Let's just not build them, this is just a broken
# prehistoric version of broken crap anyway
Patch4:		gtksourceview-2.11.2-no-tests.patch
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  gnome-common
BuildRequires:  pkgconfig(libxml-2.0)

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libname}
Summary:	Source code viewing library
Group:		Editors
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{devname}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
GtkSourceView development files.

%prep
%setup -qn gtksourceview-%{version}
%autopatch -p1

libtoolize --force
aclocal -I m4
automake -a
autoconf

%build
%configure --disable-introspection
%make

%install
%makeinstall_std
%find_lang gtksourceview-%{api}

%files -f gtksourceview-%{api}.lang
%doc AUTHORS NEWS README
%{_datadir}/gtksourceview-%{api}

%files -n %{libname}
%{_libdir}/libgtksourceview-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/gtksourceview-2.0
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

