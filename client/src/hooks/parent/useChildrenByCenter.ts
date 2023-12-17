import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { useQuery, UseQueryResult } from 'react-query';
import { Child } from 'types/generated';

export default function useChildrenByCenter(
  center_id: string,
): UseQueryResult<AxiosResponse<Child[]>, AxiosError<{ message: string }>> {
  const client = useClient();

  const getChildren = () => {
    return client.get(`parents/children/${center_id}`);
  };

  return useQuery(['children', center_id], getChildren);
}
