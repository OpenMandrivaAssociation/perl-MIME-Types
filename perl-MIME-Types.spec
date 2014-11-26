%define	upstream_name	 MIME-Types
%define upstream_version 2.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	MIME::Types module for Perl

License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More) >= 0.47

BuildArch:	noarch

%description
This Perl module maintains a set of MIME::Type objects, which each describe one
known mime type.  There are many types defined by RFCs and vendors, so the list
is long but not complete.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorlib}/MojoX

%files
%doc README ChangeLog
%{perl_vendorlib}/MIME
%{_mandir}/*/*
