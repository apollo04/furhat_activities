import { AxiosError, AxiosResponse } from 'axios';
import { useQuery, UseQueryResult } from 'react-query';
import { Child } from 'types/generated';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useChildren(): UseQueryResult<
  AxiosResponse<{ children: Child[] }>,
  AxiosError<{ message: string }>
> {
  const getChildren = () => {
    return axiosUnauthorizedInstance.get(`/children/`);
  };

  return useQuery(['children'], getChildren);
}
