import React from 'react';

import { createStyles } from '@mantine/core';

const useStyles = createStyles((theme) => ({
  wrapper: {
    height: '100%',
    minHeight: '100vh',
    display: 'flex',
    flexFlow: 'column',
    justifyContent: 'center',
    gap: `calc(${theme.spacing.xl} * 2)`,
    padding: `${theme.spacing.xl} ${theme.spacing.md}`,
  },
}));

const PublicLayout = ({ children }: { children: React.ReactNode }) => {
  const { classes } = useStyles();

  return <div className={classes.wrapper}>{children}</div>;
};

export default PublicLayout;
