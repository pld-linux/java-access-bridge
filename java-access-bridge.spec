Summary:	Assistive technology for Java Swing applications
Summary(pl):	Technologia wspomagaj±ca dla aplikacji Java Swing
Name:		java-access-bridge
Version:	1.3.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	c7b8c151661304418261be508d0daa7c
Patch0:		%{name}-jar_dir.patch
URL:		http://www.gnome.org/
BuildRequires:	at-spi-devel >= 1.3.9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	java >= 1.4
BuildRequires:	jdk >= 1.4
BuildRequires:	jre
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Java Access Bridge for GNOME, which connects
the built-in accessibility support in Java Swing apps to the GNOME
Accessibility framework, specifically the Assistive Technology Service
Provider Interface (at-spi).

%description -l pl
Ten pakiet zawiera Java Access Bridge dla GNOME, ³±cz±cy technologiê
wspieraj±c± w aplikacjach Java Swing z mechanizmami dostêpno¶ci GNOME,
w szczególno¶ci z at-spi.

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
%{_datadir}/java/*
