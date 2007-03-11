Summary:	Simple DVD mastering GUI
Summary(pl.UTF-8):	Proste GUI do nagrywania DVD
Name:		TkDVD
Version:	4.0.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://regis.damongeot.free.fr/tkdvd/dl/tkdvd-%{version}.tar.gz
# Source0-md5:	c04264f168a955ac223aad6ff98fedd4
URL:		http://regis.damongeot.free.fr/tkdvd/
Source1:	%{name}.desktop
BuildRequires:	tcl
Requires:	dvd+rw-tools
Requires:	tk >= 8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TkDVD is a GUI for growisofs which is a part of dvd+rw-tools. It
allows burning DVD+R/RW, -R/W and DVD+R DL easily.

%description -l pl.UTF-8
TkDVD jest graficzną nakładką na growisofs, które jest częścią
dvd+rw-tools. Pozwala na łatwe wypalanie DVD+R/RW, -R/W oraz DVD+R DL.

%prep
%setup -q -n tkdvd
%configure \
	%{_prefix} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name}/src}
sed  's|${source_directory}|%{_datadir}/%{name}|' TkDVD.sh \
    > $RPM_BUILD_ROOT%{_bindir}/TkDVD
rm -rf src/CVS
install src/* $RPM_BUILD_ROOT%{_datadir}/%{name}/src
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icons/tkdvd-48.png $RPM_BUILD_ROOT%{_pixmapsdir}/tkdvd.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README TODO doc/config_file
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
