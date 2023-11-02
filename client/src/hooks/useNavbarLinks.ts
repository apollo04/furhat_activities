import {
  IconReportAnalytics,
  IconNotes,
  IconSettings,
  TablerIconsProps,
  IconHome,
} from '@tabler/icons-react';

type NavbarLink = {
  label: string;
  path: string;
  Icon: (props: TablerIconsProps) => JSX.Element;
};

const specialistItems: NavbarLink[] = [
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

export default function useNavbarLinks(
  role: 'specialist' | 'parent',
): NavbarLink[] {
  if (role === 'specialist') {
    return specialistItems;
  }
  if (role === 'parent') {
    return parentItems;
  }
  return [];
}
