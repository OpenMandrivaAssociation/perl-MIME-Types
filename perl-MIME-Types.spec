%define	module	MIME-Types
%define	name	perl-%{module}
%define	modprefix MIME

%define	version	1.24
%define	release %mkrel 2

Name:		%{name}
Summary:	MIME::Types module for Perl
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::More) >= 0.47
Buildarch:	noarch

%description
This Perl module maintains a set of MIME::Type objects, which each describe one
known mime type.  There are many types defined by RFCs and vendors, so the list
is long but not complete.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*


