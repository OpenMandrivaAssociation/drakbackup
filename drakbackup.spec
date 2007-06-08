%define drakxtools_required_version  10.4.89-1mdv2007.0
%define drakxtools_conflicted_version  10.4.88

%define libname %mklibname %{name}

Summary:  Backup and restore the system
Name:     drakbackup
Version:  0.7
Release:  %mkrel 1
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    System/Configuration/Other
Url:      http://www.mandrivalinux.com/en/cvs.php3
BuildRequires: perl-MDK-Common-devel
Requires: drakxtools => %drakxtools_required_version
Requires: common-licenses
BuildRoot: %_tmppath/%name-%version-buildroot
# for program:
Conflicts: drakxtools <= %drakxtools_conflicted_version
# for man pages:
Conflicts: drakxtools-curses <= %drakxtools_conflicted_version
BuildArch: noarch

%description
Drakbackup enables to  backup and restore the system.

%prep
%setup -q

%build

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

#install lang
%find_lang %name

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog
%_sbindir/*
/usr/lib/libDrakX/icons/*
/usr/share/libDrakX/pixmaps/*
/usr/share/applications/drakbackup.desktop
%_mandir/*/*


