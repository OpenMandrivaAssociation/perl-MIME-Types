%define	upstream_name	 MIME-Types
%define	upstream_version 1.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	MIME::Types module for Perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::More) >= 0.47

Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This Perl module maintains a set of MIME::Type objects, which each describe one
known mime type.  There are many types defined by RFCs and vendors, so the list
is long but not complete.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/MIME
%{_mandir}/*/*
