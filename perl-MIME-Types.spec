%define	upstream_name	 MIME-Types
%define upstream_version 1.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	MIME::Types module for Perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

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

%files
%doc README ChangeLog
%{perl_vendorlib}/MIME
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.310.0-4mdv2012.0
+ Revision: 765485
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.310.0-3
+ Revision: 763979
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.310.0-2
+ Revision: 667243
- mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.31

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.300.0-2mdv2011.0
+ Revision: 564738
- rebuild for perl 5.12.1

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 552410
- update to 1.30

* Wed Mar 17 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.0-1mdv2010.1
+ Revision: 523435
- update to 1.29

* Mon Sep 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.0
+ Revision: 432353
- update to 1.28

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.0
+ Revision: 406379
- rebuild using %%perl_convert_version

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2009.1
+ Revision: 337657
- update to new version 1.27

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2009.1
+ Revision: 320436
- update to new version 1.26

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2009.1
+ Revision: 309310
- update to new version 1.25

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.24-2mdv2009.0
+ Revision: 265417
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.0
+ Revision: 210844
- update to new version 1.24

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2008.1
+ Revision: 132042
- update to new version 1.23

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2008.1
+ Revision: 109548
- update to new version 1.22

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2008.1
+ Revision: 97513
- update to new version 1.21

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2008.0
+ Revision: 46651
- update to new version 1.20

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.19-1mdv2008.0
+ Revision: 20278
- 1.19


* Wed Aug 16 2006 Scott Karns <scottk@mandriva.org>
+ 08/16/06 14:50:38 (56411)
Version 1.17

* Wed Aug 16 2006 Scott Karns <scottk@mandriva.org>
+ 08/16/06 14:24:49 (56395)
Import perl-MIME-Types

* Tue May 16 2006 Scott Karns <scottk@mandriva.org> 1.16-3mdk
- Modify specfile to comply with Mandriva perl packaging policy

* Fri Mar 31 2006 Buchan Milne <bgmilne@mandriva.org> 1.16-2mdk
- Rebuild
- use mkrel

* Mon Oct 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.16-1mdk
- 1.16

* Fri May 06 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.15-1mdk
- 1.15
- Change summary
- Add ChangeLog in docs

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.13-1mdk
- 1.13
- wipe buildroot in %%install, not %%prep
- cosmetics

* Sat Nov 15 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.07-2mdk
- Franck Villaume <fvill@freesurf.fr>
  - add BuildRequires : perl-devel

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 1.07-1mdk
- 1.07.

