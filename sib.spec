Summary:	simple IPX bridge
Summary(pl):	prosty tunel IPX
Name:		sib
Version:	1.1
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://members.aon.at/stsz/sib/%{name}-%{version}.tar.gz
URL:		http://members.aon.at/stsz/sib/
BuildRequires:	lzo-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIB - simple IPX bridge - is a tool for tunneling IPX (and even IP and
802.3) via UDP over a public network (e.g. Internet). It is able to
put the interface it listens on to promiscous mode, so all frames (not
only broadcasts, and frames for the tunneling server) can be received.

%description -l pl
SIB - prosty most IPX - to narzêdzie pozwalaj±ce na tunelowanie IPX (a
nawet IP oraz 802.3) przy u¿yciu UDP poprzez publiczn± sieæ (np.
Internet). Program potrafi uaktywniæ tryb promiscous na interfejsie
sieciowym dziêki czemu wszystkie ramki (nie tylko broadcasty czy ramki
do serwera tuneluj±cego) mog± byæ tunelowane.

%prep
%setup -q

%build
%{__make} GPPOPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install bin/sib	$RPM_BUILD_ROOT%{_sbindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COMPABILITY README THANKS TODO
%attr(755,root,root) %{_sbindir}/*
