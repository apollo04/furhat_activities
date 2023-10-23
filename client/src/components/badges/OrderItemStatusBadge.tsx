import { useMemo } from 'react';

import { Badge, BadgeProps } from '@mantine/core';
import { OrderItem } from 'types/generated';

interface OrderItemStatusBadgeProps
  extends Omit<BadgeProps, 'color' | 'children'> {
  status: OrderItem['status'];
}

const OrderItemStatusBadge = ({
  status,
  ...badgeProps
}: OrderItemStatusBadgeProps) => {
  const color: BadgeProps['color'] = useMemo(() => {
    if (status === 'created') return 'blue';
    if (status === 'confirmed') return 'cyan';
    if (status === 'paid') return 'green';
    if (status === 'collected') return 'teal';
    if (status === 'checked') return 'pink';
    if (status === 'delivered') return 'indigo';
    if (status === 'finished') return 'lime';
    if (status === 'canceled') return 'red';

    return 'blue';
  }, [status]);

  return (
    <Badge color={color} {...badgeProps}>
      {status}
    </Badge>
  );
};

export default OrderItemStatusBadge;
