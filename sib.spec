Summary:	simple IPX bridge
Summary(pl.UTF-8):   prosty tunel IPX
Name:		sib
Version:	1.2
Release:	2
License:	GPL
Group:		Daemons
#Source0Download: http://members.aon.at/stsz/sib/download.html
Source0:	http://members.aon.at/stsz/sib/%{name}-%{version}.tar.gz
# Source0-md5:	ab9aed3f65676c3d9fc441dbefb12320
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-lzo2.patch
URL:		http://members.aon.at/stsz/sib/
BuildRequires:	libstdc++-devel
BuildRequires:	lzo-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIB - simple IPX bridge - is a tool for tunneling IPX (and even IP and
802.3) via UDP over a public network (e.g. Internet). It is able to
put the interface it listens on to promiscous mode, so all frames (not
only broadcasts, and frames for the tunneling server) can be received.

%description -l pl.UTF-8
SIB - prosty most IPX - to narzędzie pozwalające na tunelowanie IPX (a
nawet IP oraz 802.3) przy użyciu UDP poprzez publiczną sieć (np.
Internet). Program potrafi uaktywnić tryb promiscous na interfejsie
sieciowym dzięki czemu wszystkie ramki (nie tylko broadcasty czy ramki
do serwera tunelującego) mogą być tunelowane.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	LIB="%{_lib}" \
	GPPC="%{__cxx}" \
	GPPOPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install bin/sib	$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COMPATIBILITY ChangeLog README THANKS TODO
%attr(755,root,root) %{_sbindir}/*
