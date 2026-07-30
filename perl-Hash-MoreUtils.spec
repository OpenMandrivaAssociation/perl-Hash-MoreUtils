%define upstream_name    Hash-MoreUtils
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

