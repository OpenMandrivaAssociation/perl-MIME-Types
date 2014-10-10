%define	modname	MIME-Types
%define modver 2.04

Summary:	MIME::Types module for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/MIME/MIME-Types-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More) >= 0.47

%description
This Perl module maintains a set of MIME::Type objects, which each describe one
known mime type.  There are many types defined by RFCs and vendors, so the list
is long but not complete.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{perl_vendorlib}/MIME
%{_mandir}/man3/*



