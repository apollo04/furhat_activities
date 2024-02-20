import { useState } from 'react';

import { Group, Image, Paper, Stack, Title } from '@mantine/core';

import './CategoryCard.css';
import CategoryModal from './CategoryModal.tsx';

interface CategoryCardProps {
  imgSrc: string;
  name: string;
  robotInfo?: {
    ip: string;
    name: string;
  };
}

const CategoryCard = ({ imgSrc, name, robotInfo }: CategoryCardProps) => {
  const [open, setOpen] = useState(false);
  const handleOpen = () => {
    setOpen(true);
  };

  return (
    <>
      <Paper
        onClick={handleOpen}
        shadow='md'
        className='categoryCard'
        style={{ cursor: 'pointer' }}
        sx={{ position: 'relative', overflow: 'hidden' }}
      >
        <Group
          position='right'
          pt='xs'
          px='xs'
          sx={{
            position: 'absolute',
            left: 0,
            top: 0,
            right: 0,
            zIndex: 10,
          }}
        ></Group>
        <Image
          src={`data:image/png;base64,${imgSrc}`}
          width='100%'
          height={160}
          alt={name}
        />

        <Stack pt='xs' pb='sm' px='md' spacing='xs'>
          <Title order={5} weight={700}>
            {name.charAt(0).toUpperCase() + name.slice(1)}
          </Title>
        </Stack>
      </Paper>

      <CategoryModal
        opened={open}
        onClose={() => setOpen(false)}
        size='xl'
        category={name}
        robotInfo={robotInfo}
      />
    </>
  );
};

export default CategoryCard;
