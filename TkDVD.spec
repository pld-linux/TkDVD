Summary:	Simple DVD mastering GUI
Summary(pl):	Proste GUI do nagrywania DVD
Name:		TkDVD
Version:	3.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://regis.damongeot.free.fr/tkdvd/dl/%{name}-%{version}.tar.gz
# Source0-md5:	6e750649f9607f1cdba59674cf8cfb71
URL:		http://regis.damongeot.free.fr/tkdvd/
BuildRequires:	sed
Requires:	tk >= 8.4
Requires:	dvd+rw-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TkDVD is a GUI for growisofs which is a part of dvd+rw-tools. It
allows burnning DVD+R/RW, -R/W and DVD+R DL easily.

%description -l pl
TkDVD jest graficzn± nak³adk± na growisofs, które jest cze¶ci±
dvd+rw-tools. Pozwala na ³atwe wypalanie DVD+R/RW, -R/W oraz DVD+R DL.

%prep
%setup -q -n TkDVD

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/src}
sed  's|${source_directory}|%{_datadir}/%name|' TkDVD.sh \
    > $RPM_BUILD_ROOT/%{_bindir}/TkDVD
install src/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README TODO doc/config_file
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
