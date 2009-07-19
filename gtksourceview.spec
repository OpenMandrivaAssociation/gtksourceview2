%define api_version	2.0
%define lib_major 0
%define libname	%mklibname %{name}- %{api_version} %{lib_major}
%define libnamedev %mklibname -d %{name}- %{api_version}


Summary:	Source code viewing library
Name:		gtksourceview
Version: 2.7.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Editors
URL:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	libgtk+2-devel >= 2.3.0
BuildRequires:  gtk-doc
BuildRequires:  intltool
Conflicts:		gtksourceview-sharp <= 0.5-3mdk

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
Obsoletes:	libgtksourceview0
Provides:   libgtksourceview1.0 = %{version}-%{release}
Obsoletes:  libgtksourceview1.0

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libnamedev}
Summary:        Libraries and include files for GtkSourceView
Group:          Development/GNOME and GTK+
Requires:       %{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Obsoletes: %mklibname -d  %{name}- 2.0 0

%description -n %{libnamedev}
GtkSourceView development files 


%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%{find_lang} %{name}-%{api_version}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}-%{api_version}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_datadir}/gtksourceview-%{api_version}

%files -n %{libname} 
%defattr(-,root,root)
%{_libdir}/libgtksourceview-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/gtksourceview-2.0
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*


