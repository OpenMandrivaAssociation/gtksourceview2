%define url_ver %(echo %{version}|cut -d. -f1,2)

%define _disable_rebuild_configure 1

%define api	2.0
%define major	0
%define libname %mklibname %{name}- %{api} %{major}
%define devname %mklibname -d %{name}- %{api}

Summary:	Source code viewing library
Name:		gtksourceview
Version:	2.11.2
Release:	16
License:	GPLv2+
Group:		Editors
Url:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtksourceview/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		gtksourceview-2.11-fix-GCONST-def.patch
Patch2: 	gtksourceview-2.11-glib-unicode-constant.patch
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)

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
%setup -q
%apply_patches

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std
%find_lang %{name}-%{api}

%files -f %{name}-%{api}.lang
%doc AUTHORS NEWS README
%{_datadir}/gtksourceview-%{api}

%files -n %{libname}
%{_libdir}/libgtksourceview-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/gtksourceview-2.0
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

