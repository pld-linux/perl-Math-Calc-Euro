#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Calc-Euro
Summary:	Math::Calc::Euro - convert between Euro and the old currencies
Summary(pl.UTF-8):	Math::Calc::Euro - przeliczanie między Euro i starymi walutami
Name:		perl-Math-Calc-Euro
Version:	0.02
Release:	3
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	975bc78efc86ff4598988b13265bf26f
URL:		http://search.cpan.org/dist/Math-Calc-Euro/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Math::Calc::Euro module provides for an object oriented interface
for converting to/from Euro.

%description -l pl.UTF-8
Moduł Math::Calc::Euro udostępnia obiektowo zorientowany interfejs do
przeliczania na/z Euro.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
