%include	/usr/lib/rpm/macros.perl
Summary:	Nagios Console Monitor
Summary(pl.UTF-8):	Konsola monitorująca dla Nagiosa
Name:		nagios-nsc
Version:	0.80
Release:	2
License:	Artistic
Group:		Applications
Source0:	http://dl.sourceforge.net/nsc-gothix/nsc-%{version}-2.tar.gz
# Source0-md5:	fec6de9a07d8b1b2f5fd106d7fc8a5ed
Patch0:		nsc-path.patch
Patch1:		warnings_new-log-format.patch
URL:		http://sourceforge.net/projects/nsc-gothix/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nsc is a curses-based tty/console monitor for Nagios v1/v2. It allows
you to monitor Nagios services without the expense or availability of
a GUI and features a full-screen realtime colourized display of Nagios
service status.

%description -l pl.UTF-8
nsc to oparty na curses działający na konsoli/terminalu monitor dla
Nagiosa v1/v2. Pozwala monitorować usługi Nagiosa bez kosztu lub
dostępności GUI, oferuje pełnoekranowy, kolorowy podgląd w czasie
rzeczywistym stanu usług Nagiosa.

%prep
%setup -q -n nsc
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{perl_vendorlib}}

install nsc.pl $RPM_BUILD_ROOT%{_bindir}/nsc
install nsc.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a gothix $RPM_BUILD_ROOT%{perl_vendorlib}
install nsc_nagios.pm $RPM_BUILD_ROOT%{perl_vendorlib}/nsc_nagios.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/nsc
%{_mandir}/man1/nsc.1*
%{perl_vendorlib}/gothix
%{perl_vendorlib}/nsc_nagios.pm
