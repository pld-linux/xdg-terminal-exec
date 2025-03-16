Summary:	Reference implementation for XDG Default Terminal Execution Specification proposal
Summary(pl.UTF-8):	Implementacja referencyjna propozycji specifikacji XDG Default Terminal Execution
Name:		xdg-terminal-exec
Version:	0.12.3
Release:	2
License:	GPL v3+
Group:		Applications
#Source0Download: https://github.com/Vladimir-csp/xdg-terminal-exec/tags
Source0:	https://github.com/Vladimir-csp/xdg-terminal-exec/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d4c77776c379cf121aab4fd24ffeddd9
URL:		https://github.com/Vladimir-csp/xdg-terminal-exec
BuildRequires:	scdoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proposal for XDG Default Terminal Execution Specification and
reference shell-based implementation.

%description -l pl.UTF-8
Propozycja specifikacji XDG Default Terminal Execution (uruchamiania
domyślnego terminala) wraz z implementacją referencyjną opartą na
powłoce.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/xdg-terminal-exec
%{_datadir}/xdg-terminal-exec
%{_mandir}/man1/xdg-terminal-exec.1*
