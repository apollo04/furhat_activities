import {
  // IconSettings,
  TablerIconsProps,
  IconHome,
  IconUsers,
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
    label: 'Students',
    path: '/students',
    Icon: IconUsers,
  },
  // {
  //   label: 'Settings',
  //   path: '/settings',
  //   Icon: IconSettings,
  // },
];

export default function useNavbarLinks(): NavbarLink[] {
  return specialistItems;
}
