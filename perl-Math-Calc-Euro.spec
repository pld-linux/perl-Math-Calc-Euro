#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Calc-Euro
Summary:	Math::Calc::Euro - convert between EUR and the old currencies
Summary(pl):	Math::Calc::Euro - przeliczanie miêdzy EUR i starymi walutami
Name:		perl-Math-Calc-Euro
Version:	0.02
Release:	2
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Math::Calc::Euro module provides for an object oriented interface
for converting to/from EUR.

%description -l pl
Modu³ Math::Calc::Euro udostêpnia obiektowo zorientowany interfejs do
przeliczania na/z EUR.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Calc/Euro.pm
%{_mandir}/man3/*
