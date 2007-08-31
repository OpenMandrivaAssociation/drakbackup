%define drakxtools_required_version  10.4.89-1mdv2007.0
%define drakxtools_conflicted_version  10.4.88

%define libname %mklibname %{name}

Summary:  Backup and restore the system
Name:     drakbackup
Version:  0.9
Release:  %mkrel 2
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
cat > %{buildroot}%{_sysconfdir}/pam.d/drakbackup <<EOF
#%PAM-1.0
auth       sufficient   pam_rootok.so
auth       required     pam_console.so
auth       sufficient   pam_timestamp.so
auth       include      system-auth
account    required     pam_permit.so
session    required     pam_permit.so
session    optional     pam_xauth.so
session    optional     pam_timestamp.so
EOF
sed -i -e "s,%{_sbindir}/drakbackup,%{_bindir}/drakbackup," \
        %{buildroot}%{_datadir}/applications/drakbackup.desktop

%post
%update_menus

%postun
%clean_menus

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

