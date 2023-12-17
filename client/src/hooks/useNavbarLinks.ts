import {
  IconReportAnalytics,
  IconNotes,
  IconSettings,
  TablerIconsProps,
  IconHome,
  IconUsers,
} from '@tabler/icons-react';

type NavbarLink = {
  label: string;
  path: string;
  Icon: (props: TablerIconsProps) => JSX.Element;
};

const parentItems: NavbarLink[] = [
  {
    label: 'Dashboard',
    path: '/',
    Icon: IconHome,
  },
  {
    label: 'Grades',
    path: '/grades',
    Icon: IconReportAnalytics,
  },
  {
    label: 'Skills',
    path: '/skills',
    Icon: IconNotes,
  },
  {
    label: 'Settings',
    path: '/settings',
    Icon: IconSettings,
  },
];

const specialistItems: NavbarLink[] = [
  {
    label: 'Dashboard',
    path: '/',
    Icon: IconHome,
  },
  {
    label: 'Students',
    path: '/students',
    Icon: IconUsers,
  },
  {
    label: 'Settings',
    path: '/settings',
    Icon: IconSettings,
  },
];

const adminItems: NavbarLink[] = [
  {
    label: 'Centers',
    path: '/',
    Icon: IconHome,
  },
];

export default function useNavbarLinks(
  role: 'specialist' | 'parent',
): NavbarLink[] {
  if (role === 'specialist') {
    return specialistItems;
  }
  if (role === 'parent') {
    return parentItems;
  }
  if (role === 'admin') {
    return adminItems;
  }
  return [];
}
