%define drakxtools_required_version  10.4.89-1mdv2007.0
%define drakxtools_conflicted_version  10.4.88

%define libname %mklibname %{name}

Summary:  Backup and restore the system
Name:     drakbackup
Version:  0.19.3
Release:  %mkrel 2
Source0:  %name-%version.tar.lzma
License:  GPL
Group:    Archiving/Other
Url:      http://www.mandrivalinux.com/en/cvs.php3
BuildRequires: perl-MDK-Common-devel
Requires: drakxtools => %drakxtools_required_version
Requires: common-licenses
Requires: usermode-consoleonly >= 1.92-4mdv2008.0
BuildRoot: %_tmppath/%name-%version-buildroot
# for program:
Conflicts: drakxtools <= %drakxtools_conflicted_version
# for man pages:
Conflicts: drakxtools-curses <= %drakxtools_conflicted_version
BuildArch: noarch

%description
Drakbackup enables to backup and restore the system.

%prep
%setup -q

%build

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

#install lang
%find_lang %name

# consolehelper configuration
# ask for root password
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/drakbackup
mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
cat > %{buildroot}%{_sysconfdir}/security/console.apps/drakbackup <<EOF
USER=root
PROGRAM=/usr/sbin/drakbackup
FALLBACK=false
SESSION=true
EOF
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
ln -sf %{_sysconfdir}/pam.d/mandriva-simple-auth %{buildroot}%{_sysconfdir}/pam.d/drakbackup
# make menu entry call the consolehelper link
sed -i -e "s,%{_sbindir}/drakbackup,%{_bindir}/drakbackup," \
        %{buildroot}%{_datadir}/applications/drakbackup.desktop

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) %_sysconfdir/pam.d/drakbackup
%config(noreplace) %_sysconfdir/security/console.apps/drakbackup
%_bindir/drakbackup
%_sbindir/*
/usr/lib/libDrakX/icons/*
/usr/share/libDrakX/pixmaps/*
/usr/share/applications/drakbackup.desktop
%_mandir/*/*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.19.3-2mdv2011.0
+ Revision: 610272
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.19.3-1mdv2010.1
+ Revision: 546251
- 0.19.3
- translation updates

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.19.2-2mdv2010.0
+ Revision: 413377
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.19.2-1mdv2009.1
+ Revision: 367398
- translation updates

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.19.1-1mdv2009.1
+ Revision: 362302
- translation updates

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.19-2mdv2009.1
+ Revision: 350835
- rebuild

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 0.19-1mdv2009.0
+ Revision: 289960
- translation updates

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.18-1mdv2009.0
+ Revision: 286965
- translation updates

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.17-1mdv2009.0
+ Revision: 218424
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.17-1mdv2008.1
+ Revision: 192102
- translation updates

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.16-1mdv2008.1
+ Revision: 190115
- translation updates

* Wed Feb 27 2008 Thierry Vignaud <tv@mandriva.org> 0.15-1mdv2008.1
+ Revision: 175860
- translation updates
- translation updates

* Thu Feb 21 2008 Thierry Vignaud <tv@mandriva.org> 0.14-3mdv2008.1
+ Revision: 173673
- better group

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.14-2mdv2008.1
+ Revision: 149218
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 0.14-1mdv2008.0
+ Revision: 95037
- updated translation

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 0.13-1mdv2008.0
+ Revision: 94271
- updated translation

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 0.12-1mdv2008.0
+ Revision: 92935
- updated translations

* Tue Sep 18 2007 Thierry Vignaud <tv@mandriva.org> 0.11-1mdv2008.0
+ Revision: 89797
- fix encoding of "No device found"
- hide menu entry
- fix encoding of "No device found"
- hide menu entry
- fix spacing in description

* Sat Sep 15 2007 Thierry Vignaud <tv@mandriva.org> 0.10-1mdv2008.0
+ Revision: 86704
- fix multiple keys named "Icon" in group "Desktop Entry"
- updated translation
- wrap a too big label

* Wed Sep 12 2007 Andreas Hasenack <andreas@mandriva.com> 0.9-3mdv2008.0
+ Revision: 84832
- use new common pam config files for usermode/consolehelper

* Fri Aug 31 2007 Andreas Hasenack <andreas@mandriva.com> 0.9-2mdv2008.0
+ Revision: 77137
- ask console user for root password
- adjust menu entry to point to bindir instead of sbindir
  so we use consolehelper directly

* Thu Aug 02 2007 Thierry Vignaud <tv@mandriva.org> 0.9-1mdv2008.0
+ Revision: 57895
- disable notifications (#18965)
- fix detecting DVD drives (#28946)
- offer more sizes (dual layer DVD, Blu-Ray -R, HD DVD-R) (#29918)

* Wed Aug 01 2007 Thierry Vignaud <tv@mandriva.org> 0.8-1mdv2008.0
+ Revision: 57771
- fix detecting tape devices with newer kernel (#31073)
- use a saner/more robust tape detection
- use a shorter button label (#31771)

* Fri Jun 08 2007 Thierry Vignaud <tv@mandriva.org> 0.7-1mdv2008.0
+ Revision: 37476
- first release after SVN recover
- do not package anymore COPYING


* Wed Apr 04 2007 Stew Benedict <sbenedict@mandriva.com> 0.6-2mdv2007.1
+ Revision: 150538
- Fix Group

* Thu Mar 08 2007 Stew Benedict <sbenedict@mandriva.com> 0.6-1mdv2007.1
+ Revision: 137777
- bump to 0.6

* Sun Feb 25 2007 Stew Benedict <sbenedict@mandriva.com> 0.5-1mdv2007.1
+ Revision: 125653
- Update the Changelog a bit too
- fix tarball Makefile
- bump to 0.5
  Drop ATAPI argument for wodim
  Allow writing direct to CD/DVD with no intermediate ISO image
  Allow using -force argument for wodim (had to use locally for some slow media)
  Handle gzipped file lists correctly
  We don't need to own drakconnect man pages

* Fri Feb 23 2007 Stew Benedict <sbenedict@mandriva.com> 0.4-1mdv2007.1
+ Revision: 125132
- remove old tarballs
  Fix for #28489 (user defined BLOCK_SIZE env var -> commas in df output)
  Fix categories in .desktop file (fcrozat)
- bump to 0.4

* Sun Feb 18 2007 Stew Benedict <sbenedict@mandriva.com> 0.3-1mdv2007.1
+ Revision: 122504
- 0.3 - fix for migration from cdrecord -> cdrkit (#28526)

* Sat Feb 17 2007 Stew Benedict <sbenedict@mandriva.com> 0.2-1mdv2007.1
+ Revision: 122178
- 0.2 - fixes for #27780, #27783, #28656

* Fri Jan 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-2mdv2007.1
+ Revision: 110744
- do not require printerdrake

* Tue Jan 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2007.1
+ Revision: 106617
- Import drakbackup

* Thu Nov 30 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0-1mdv2007.1
- initial release (splited out of drakxtools)

