# requires Java >= 1.5 < 11 (idlj removed in Java 11)
%define		use_jdk		openjdk8

Summary:	Assistive technology for Java Swing applications
Summary(pl.UTF-8):	Technologia wspomagająca dla aplikacji Java Swing
Name:		java-access-bridge
Version:	1.26.2
Release:	1
License:	LGPL v2+
Group:		Libraries/Java
Source0:	https://download.gnome.org/sources/java-access-bridge/1.26/%{name}-%{version}.tar.bz2
# Source0-md5:	baeac0a4f26f66996f62ffa88d6cd19e
Patch0:		%{name}-jar_dir.patch
URL:		https://wiki.gnome.org/Attic/Java%20Access%20Bridge
# headers + idl files
BuildRequires:	at-spi >= 1.22.0
BuildRequires:	at-spi-devel >= 1.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0
%buildrequires_jdk
BuildRequires:	libbonobo-devel >= 2.22.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.021
BuildRequires:	xorg-app-xprop
Requires:	jpackage-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Java Access Bridge for GNOME, which connects
the built-in accessibility support in Java Swing apps to the GNOME
Accessibility framework, specifically the Assistive Technology Service
Provider Interface (at-spi).

%description -l pl.UTF-8
Ten pakiet zawiera Java Access Bridge dla GNOME, łączący technologię
wspierającą w aplikacjach Java Swing z mechanizmami dostępności GNOME,
w szczególności z at-spi.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--with-java-home=%{java_home}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libjava-access-bridge-jni.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libjava-access-bridge-jni.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjava-access-bridge-jni.so.0
%attr(755,root,root) %{_libdir}/libjava-access-bridge-jni.so
%{_javadir}/JNav.jar
%{_javadir}/gnome-java-bridge.jar
%{_javadir}/accessibility.properties
