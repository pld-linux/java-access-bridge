Summary:	Assistive technology for Java Swing applications
Summary(pl.UTF-8):   Technologia wspomagająca dla aplikacji Java Swing
Name:		java-access-bridge
Version:	1.6.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/java-access-bridge/1.6/%{name}-%{version}.tar.bz2
# Source0-md5:	a8d7312bbc5a3398edf16b17e50463f7
Patch0:		%{name}-jar_dir.patch
URL:		http://www.gnome.org/
BuildRequires:	at-spi-devel >= 1.7.10
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	java >= 1.4
BuildRequires:	jdk >= 1.4
BuildRequires:	jre
BuildRequires:	libbonobo-devel >= 2.16.0
BuildArch:	noarch
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_javadir}/*
