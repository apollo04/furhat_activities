import { useMemo } from 'react';

import { Badge, BadgeProps } from '@mantine/core';
import { Order } from 'types/generated';

interface OrderStatusBadgeProps extends Omit<BadgeProps, 'color' | 'children'> {
  status: Order['status'];
}

const OrderStatusBadge = ({ status, ...badgeProps }: OrderStatusBadgeProps) => {
  const color: BadgeProps['color'] = useMemo(() => {
    if (status === 'created') return 'blue';
    if (status === 'approved') return 'cyan';
    if (status === 'assigned') return 'green';
    if (status === 'in_progress') return 'teal';
    if (status === 'finished') return 'lime';
    if (status === 'canceled') return 'red';

    return 'blue';
  }, [status]);

  const statusToDisplay = useMemo(() => {
    if (status === 'in_progress') return 'in progress';

    return status;
  }, [status]);

  return (
    <Badge color={color} {...badgeProps}>
      {statusToDisplay}
    </Badge>
  );
};

export default OrderStatusBadge;
