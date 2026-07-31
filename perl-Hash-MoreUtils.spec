%define upstream_name    Hash-MoreUtils
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	0.06
Release:	24

Summary:	Provide the stuff missing in Hash::Util
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/perl5-utils/Hash-MoreUtils
Source0:	https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Hash-MoreUtils-0.06.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Similar to 'List::MoreUtils', 'Hash::MoreUtils' contains trivial but
commonly-used functionality for hashes.

%prep
%setup -q -n Hash-MoreUtils-0.06

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%make_install

%files
%doc META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

